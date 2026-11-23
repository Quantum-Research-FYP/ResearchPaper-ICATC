"""
qc_ir.py - minimal shared circuit IR used by every dataset in this package.

IR (JSON-serialisable dict):
{
  "id": "E05", "name": "bell_state", "num_qubits": 2,
  "ops": [ {"g": "h", "q": [0]}, {"g": "cx", "q": [0, 1]}, {"g": "rx", "q": [0], "p": [0.3]},
           {"g": "barrier", "q": [0, 1]} ],
  "measure": [0, 1]            # qubits measured at the end, in this order ([] = no measurement)
}

Conventions (see 00_common/CONVENTIONS.md)
  * Qubit 0 is the LEFTMOST character of every canonical bitstring ("q0 q1 ... q(n-1)").
  * Controls come first in "q" (cx: [control, target]; ccx: [c1, c2, target]).
  * Rotation angles are in RADIANS (rx/ry/rz = exp(-i*theta*P/2); p = diag(1, e^{i*theta})).
  * Parameters may be a string (symbolic parameter name) only in the transpilation set (T..);
    simulation needs numeric values (use bind_params).
Supported ops:  h x y z s sdg t tdg rx ry rz p | cx cy cz swap crx cry crz cp ccx mcx3 | barrier
Not supported (documented limitation): classical conditions, mid-circuit measurement, reset.
"""
import math, re, json, copy
import numpy as np

SINGLE = {"h", "x", "y", "z", "s", "sdg", "t", "tdg", "rx", "ry", "rz", "p"}
CONTROLLED = {"cx": ("x", 1), "cy": ("y", 1), "cz": ("z", 1), "ccx": ("x", 2), "mcx3": ("x", 3),
              "crx": ("rx", 1), "cry": ("ry", 1), "crz": ("rz", 1), "cp": ("p", 1)}
PARAM_GATES = {"rx", "ry", "rz", "p", "crx", "cry", "crz", "cp"}
ARITY = {**{g: 1 for g in SINGLE}, "cx": 2, "cy": 2, "cz": 2, "swap": 2, "crx": 2, "cry": 2,
         "crz": 2, "cp": 2, "ccx": 3, "mcx3": 4}


def gate_matrix(name, theta=None):
    I = 1j
    if name == "h": return np.array([[1, 1], [1, -1]], dtype=complex) / math.sqrt(2)
    if name == "x": return np.array([[0, 1], [1, 0]], dtype=complex)
    if name == "y": return np.array([[0, -I], [I, 0]], dtype=complex)
    if name == "z": return np.array([[1, 0], [0, -1]], dtype=complex)
    if name == "s": return np.array([[1, 0], [0, I]], dtype=complex)
    if name == "sdg": return np.array([[1, 0], [0, -I]], dtype=complex)
    if name == "t": return np.array([[1, 0], [0, np.exp(I * math.pi / 4)]], dtype=complex)
    if name == "tdg": return np.array([[1, 0], [0, np.exp(-I * math.pi / 4)]], dtype=complex)
    if name == "rx":
        c, s = math.cos(theta / 2), math.sin(theta / 2)
        return np.array([[c, -I * s], [-I * s, c]], dtype=complex)
    if name == "ry":
        c, s = math.cos(theta / 2), math.sin(theta / 2)
        return np.array([[c, -s], [s, c]], dtype=complex)
    if name == "rz": return np.array([[np.exp(-I * theta / 2), 0], [0, np.exp(I * theta / 2)]], dtype=complex)
    if name == "p": return np.array([[1, 0], [0, np.exp(I * theta)]], dtype=complex)
    raise ValueError(name)


def validate(c):
    n = c["num_qubits"]
    for op in c["ops"]:
        g, q = op["g"], op["q"]
        if g == "barrier":
            continue
        if g == "swap":
            assert len(q) == 2, (c["id"], op)
        else:
            assert g in ARITY, f"unsupported gate {g} in {c['id']}"
            assert len(q) == ARITY[g], (c["id"], op)
        assert len(set(q)) == len(q) and all(0 <= x < n for x in q), (c["id"], op)
        if g in PARAM_GATES:
            assert "p" in op and len(op["p"]) == 1, (c["id"], op)
    for m in c.get("measure", []):
        assert 0 <= m < n
    return True


def used_qubits(c):
    s = set()
    for op in c["ops"]:
        if op["g"] != "barrier":
            s.update(op["q"])
    return s


def bind_params(c, values):
    c2 = copy.deepcopy(c)
    for op in c2["ops"]:
        if "p" in op:
            op["p"] = [values[x] if isinstance(x, str) else x for x in op["p"]]
    return c2


def _apply_controlled(state, U, controls, target):
    idx = [slice(None)] * state.ndim
    for ctl in controls:
        idx[ctl] = 1
    idx = tuple(idx)
    sub = state[idx]
    ax = target - sum(1 for ctl in controls if ctl < target)
    sub = np.moveaxis(np.tensordot(U, sub, axes=([1], [ax])), 0, ax)
    state[idx] = sub
    return state


def simulate(c, bind=None):
    """Exact statevector (shape (2,)*n; axis i = qubit i)."""
    if bind:
        c = bind_params(c, bind)
    n = c["num_qubits"]
    state = np.zeros((2,) * n, dtype=complex)
    state[(0,) * n] = 1.0
    for op in c["ops"]:
        g, q = op["g"], op["q"]
        if g == "barrier":
            continue
        th = op["p"][0] if "p" in op else None
        if isinstance(th, str):
            raise ValueError("symbolic parameter %s: pass bind={...}" % th)
        if g == "swap":
            state = np.ascontiguousarray(np.swapaxes(state, q[0], q[1]))
        elif g in SINGLE:
            state = _apply_controlled(state, gate_matrix(g, th), [], q[0])
        else:
            base, k = CONTROLLED[g]
            state = _apply_controlled(state, gate_matrix(base, th), q[:k], q[k])
    return state


def probabilities(c, bind=None, measured=None):
    """Exact distribution over canonical bitstrings of the measured qubits (default: c['measure'])."""
    st = simulate(c, bind)
    n = c["num_qubits"]
    meas = c.get("measure", list(range(n))) if measured is None else measured
    if not meas:
        meas = list(range(n))
    p = np.abs(st) ** 2
    others = tuple(q for q in range(n) if q not in meas)
    if others:
        p = p.sum(axis=others)
    srt = sorted(meas)
    p = np.transpose(p, [srt.index(q) for q in meas])
    out = {}
    for idx in np.ndindex(*p.shape):
        v = float(p[idx])
        if v > 1e-12:
            out["".join(map(str, idx))] = v
    return out


def gate_depth(c):
    """Depth over gates only (barriers and measurements ignored)."""
    lvl = [0] * c["num_qubits"]
    for op in c["ops"]:
        if op["g"] == "barrier":
            continue
        d = 1 + max(lvl[q] for q in op["q"])
        for q in op["q"]:
            lvl[q] = d
    return max(lvl) if lvl else 0


def metrics(c):
    ops = [o for o in c["ops"] if o["g"] != "barrier"]
    multi = [o for o in ops if len(o["q"]) >= 2]
    gates = sorted({o["g"] for o in ops})
    return {"num_qubits": c["num_qubits"], "gate_count": len(ops), "depth": gate_depth(c),
            "two_qubit_or_more_gates": len(multi), "gate_types": " ".join(gates),
            "n_gate_types": len(gates),
            "parameterized": "symbolic" if any(isinstance(x, str) for o in ops for x in o.get("p", [])) else
            ("fixed_angles" if any("p" in o for o in ops) else "none"),
            "n_barriers": sum(1 for o in c["ops"] if o["g"] == "barrier"),
            "measured_qubits": " ".join(map(str, c.get("measure", [])))}


# ----------------------------------------------------------------------------- OpenQASM 3 emitter
def to_qasm3(c):
    n = c["num_qubits"]
    meas = c.get("measure", [])
    syms = sorted({x for o in c["ops"] for x in o.get("p", []) if isinstance(x, str)})
    L = ["OPENQASM 3.0;", 'include "stdgates.inc";']
    L += [f"input float[64] {s};" for s in syms]
    L.append(f"qubit[{n}] q;")
    if meas:
        L.append(f"bit[{len(meas)}] c;")
    for o in c["ops"]:
        g, q = o["g"], o["q"]
        if g == "barrier":
            L.append("barrier " + ", ".join(f"q[{i}]" for i in q) + ";")
            continue
        args = ", ".join(f"q[{i}]" for i in q)
        par = ""
        if "p" in o:
            v = o["p"][0]
            par = f"({v if isinstance(v, str) else repr(float(v))})"
        if g == "mcx3":
            L.append(f"ctrl(3) @ x {args};")
        else:
            L.append(f"{g}{par} {args};")
    for i, m in enumerate(meas):
        L.append(f"c[{i}] = measure q[{m}];")
    return "\n".join(L) + "\n"


_ARGQ = re.compile(r"q\[(\d+)\]")


def qasm3_probabilities(text):
    """Tiny parser for the subset emitted by to_qasm3 (self-consistency check of the emitter)."""
    n = None; ops = []; meas = []
    for line in text.splitlines():
        line = line.strip().rstrip(";")
        if not line or line.startswith(("OPENQASM", "include", "input", "bit[")):
            continue
        m = re.match(r"qubit\[(\d+)\] q", line)
        if m:
            n = int(m.group(1)); continue
        m = re.match(r"c\[(\d+)\] = measure q\[(\d+)\]", line)
        if m:
            meas.append((int(m.group(1)), int(m.group(2)))); continue
        if line.startswith("barrier"):
            continue
        m = re.match(r"ctrl\(3\) @ x (.*)", line)
        if m:
            ops.append({"g": "mcx3", "q": [int(x) for x in _ARGQ.findall(m.group(1))]}); continue
        m = re.match(r"(\w+)(?:\(([^)]*)\))? (.*)", line)
        g, par, args = m.group(1), m.group(2), m.group(3)
        op = {"g": g, "q": [int(x) for x in _ARGQ.findall(args)]}
        if par is not None:
            op["p"] = [float(par)]
        ops.append(op)
    c = {"id": "qasm", "num_qubits": n, "ops": ops, "measure": [q for _, q in sorted(meas)]}
    return probabilities(c)


def tvd(p, q):
    keys = set(p) | set(q)
    return 0.5 * sum(abs(p.get(k, 0.0) - q.get(k, 0.0)) for k in keys)


def dumps(obj):
    return json.dumps(obj, indent=1, ensure_ascii=False)
