"""
frameworks.py - generate each framework's version of an IR circuit and run it on an ideal simulator.

STATUS: written against the public APIs of Qiskit/Qiskit-Aer, Cirq, PennyLane, pytket(+pytket-qiskit) and Amazon Braket,
but NOT executed in the environment where this package was assembled (none of these libraries was installed there).
Run `python 02_equivalence/scripts/smoke_test.py` first; it checks every framework against the exact numpy reference
for the simplest circuits and tells you which builders need adjusting for your installed versions.

Every runner returns canonical counts: {bitstring: count}, bitstring = measured qubits in the order of c["measure"],
leftmost character = first measured qubit (usually q0).
"""
import math
from collections import Counter

import numpy as np
from qc_ir import SINGLE, CONTROLLED

PI = math.pi


def _val(op):
    return op["p"][0] if "p" in op else None


# ---------------------------------------------------------------------------------------------- Qiskit
def to_qiskit(c, with_measure=True):
    """Symbolic parameters (strings) become qiskit Parameters."""
    from qiskit import QuantumCircuit
    from qiskit.circuit import Parameter
    meas = c.get("measure", [])
    qc = QuantumCircuit(c["num_qubits"], len(meas) if (meas and with_measure) else 0)
    params = {}

    def P(v):
        if isinstance(v, str):
            params.setdefault(v, Parameter(v))
            return params[v]
        return v

    for op in c["ops"]:
        g, q, v = op["g"], op["q"], _val(op)
        if g == "barrier": qc.barrier(*q)
        elif g == "mcx3": qc.mcx(q[:3], q[3])
        elif g in ("rx", "ry", "rz", "p"): getattr(qc, g)(P(v), q[0])
        elif g in ("crx", "cry", "crz", "cp"): getattr(qc, g)(P(v), q[0], q[1])
        else: getattr(qc, g)(*q)
    if meas and with_measure:
        for i, m in enumerate(meas):
            qc.measure(m, i)
    return qc


def run_qiskit(c, shots, seed):
    from qiskit_aer import AerSimulator
    qc = to_qiskit(c)
    res = AerSimulator(seed_simulator=seed).run(qc, shots=shots).result().get_counts()
    return {k.replace(" ", "")[::-1]: int(v) for k, v in res.items()}      # qiskit: clbit0 is rightmost


# ---------------------------------------------------------------------------------------------- Cirq
def to_cirq(c):
    import cirq
    qs = cirq.LineQubit.range(c["num_qubits"])
    ops = []
    for op in c["ops"]:
        g, q, v = op["g"], [qs[i] for i in op["q"]], _val(op)
        if g == "barrier": continue
        elif g == "h": ops.append(cirq.H(*q))
        elif g == "x": ops.append(cirq.X(*q))
        elif g == "y": ops.append(cirq.Y(*q))
        elif g == "z": ops.append(cirq.Z(*q))
        elif g == "s": ops.append(cirq.S(*q))
        elif g == "sdg": ops.append((cirq.S ** -1)(*q))
        elif g == "t": ops.append(cirq.T(*q))
        elif g == "tdg": ops.append((cirq.T ** -1)(*q))
        elif g == "rx": ops.append(cirq.rx(v)(*q))
        elif g == "ry": ops.append(cirq.ry(v)(*q))
        elif g == "rz": ops.append(cirq.rz(v)(*q))
        elif g == "p": ops.append(cirq.ZPowGate(exponent=v / PI)(*q))
        elif g == "cx": ops.append(cirq.CNOT(*q))
        elif g == "cy": ops.append(cirq.Y.controlled().on(*q))
        elif g == "cz": ops.append(cirq.CZ(*q))
        elif g == "swap": ops.append(cirq.SWAP(*q))
        elif g == "ccx": ops.append(cirq.CCX(*q))
        elif g == "mcx3": ops.append(cirq.X.controlled(num_controls=3).on(*q))
        elif g == "crx": ops.append(cirq.ControlledGate(cirq.rx(v)).on(*q))
        elif g == "cry": ops.append(cirq.ControlledGate(cirq.ry(v)).on(*q))
        elif g == "crz": ops.append(cirq.ControlledGate(cirq.rz(v)).on(*q))
        elif g == "cp": ops.append(cirq.CZPowGate(exponent=v / PI)(*q))
        else: raise ValueError(g)
    meas = c.get("measure", [])
    if meas:
        ops.append(cirq.measure(*[qs[m] for m in meas], key="m"))      # MEASURE THE FULL REGISTER, not only q0
    return cirq.Circuit(ops)


def run_cirq(c, shots, seed):
    import cirq
    circ = to_cirq(c)
    res = cirq.Simulator(seed=seed).run(circ, repetitions=shots)
    cnt = Counter("".join(str(int(b)) for b in row) for row in res.measurements["m"])
    return dict(cnt)


# ---------------------------------------------------------------------------------------------- PennyLane
def _pl_ops(c):
    import pennylane as qml
    for op in c["ops"]:
        g, q, v = op["g"], op["q"], _val(op)
        if g == "barrier": continue
        elif g == "h": qml.Hadamard(wires=q[0])
        elif g == "x": qml.PauliX(wires=q[0])
        elif g == "y": qml.PauliY(wires=q[0])
        elif g == "z": qml.PauliZ(wires=q[0])
        elif g == "s": qml.S(wires=q[0])
        elif g == "sdg": qml.adjoint(qml.S)(wires=q[0])
        elif g == "t": qml.T(wires=q[0])
        elif g == "tdg": qml.adjoint(qml.T)(wires=q[0])
        elif g == "rx": qml.RX(v, wires=q[0])
        elif g == "ry": qml.RY(v, wires=q[0])
        elif g == "rz": qml.RZ(v, wires=q[0])
        elif g == "p": qml.PhaseShift(v, wires=q[0])
        elif g == "cx": qml.CNOT(wires=q)
        elif g == "cy": qml.CY(wires=q)
        elif g == "cz": qml.CZ(wires=q)
        elif g == "swap": qml.SWAP(wires=q)
        elif g == "ccx": qml.Toffoli(wires=q)
        elif g == "mcx3": qml.ctrl(qml.PauliX, control=q[:3])(wires=q[3])
        elif g == "crx": qml.CRX(v, wires=q)
        elif g == "cry": qml.CRY(v, wires=q)
        elif g == "crz": qml.CRZ(v, wires=q)
        elif g == "cp": qml.ControlledPhaseShift(v, wires=q)
        else: raise ValueError(g)


def run_pennylane(c, shots, seed):
    import pennylane as qml
    meas = c.get("measure", list(range(c["num_qubits"])))
    dev = qml.device("default.qubit", wires=c["num_qubits"], shots=shots, seed=seed)

    @qml.qnode(dev)
    def circuit():
        _pl_ops(c)
        return qml.counts(wires=meas)

    return {k: int(v) for k, v in circuit().items()}


def exact_pennylane(c):
    """Exact probabilities (no shots): the analytic reference from PennyLane itself."""
    import pennylane as qml
    meas = c.get("measure", list(range(c["num_qubits"])))
    dev = qml.device("default.qubit", wires=c["num_qubits"])

    @qml.qnode(dev)
    def circuit():
        _pl_ops(c)
        return qml.probs(wires=meas)

    pr = np.array(circuit()).reshape(-1)
    n = len(meas)
    return {format(i, f"0{n}b"): float(p) for i, p in enumerate(pr) if p > 1e-12}


# ---------------------------------------------------------------------------------------------- pytket
def to_tket(c):
    """pytket angles are in HALF-TURNS (multiples of pi): every radian angle is divided by pi."""
    from pytket import Circuit, OpType
    meas = c.get("measure", [])
    t = Circuit(c["num_qubits"], len(meas))
    for op in c["ops"]:
        g, q, v = op["g"], op["q"], _val(op)
        if isinstance(v, str):
            v = math.pi / 4.0
        a = None if v is None else v / PI
        if g == "barrier": continue
        elif g == "h": t.H(q[0])
        elif g == "x": t.X(q[0])
        elif g == "y": t.Y(q[0])
        elif g == "z": t.Z(q[0])
        elif g == "s": t.S(q[0])
        elif g == "sdg": t.Sdg(q[0])
        elif g == "t": t.T(q[0])
        elif g == "tdg": t.Tdg(q[0])
        elif g == "rx": t.Rx(a, q[0])
        elif g == "ry": t.Ry(a, q[0])
        elif g == "rz": t.Rz(a, q[0])
        elif g == "p": t.Rz(a, q[0])                   # equal to p(theta) up to a global phase
        elif g == "cx": t.CX(*q)
        elif g == "cy": t.CY(*q)
        elif g == "cz": t.CZ(*q)
        elif g == "swap": t.SWAP(*q)
        elif g == "ccx": t.CCX(*q)
        elif g == "mcx3": t.add_gate(OpType.CnX, q)
        elif g == "crx": t.CRx(a, *q)
        elif g == "cry": t.CRy(a, *q)
        elif g == "crz": t.CRz(a, *q)
        elif g == "cp": t.CU1(a, *q)                   # controlled-PHASE (CRz would differ by a phase on the control)
        else: raise ValueError(g)
    for i, m in enumerate(meas):
        t.Measure(m, i)
    return t


def run_tket(c, shots, seed):
    from pytket.qasm import circuit_to_qasm_str
    from qiskit import QuantumCircuit
    from qiskit_aer import AerSimulator
    t = to_tket(c)
    qasm_str = circuit_to_qasm_str(t)
    # Fix pytket OpenQASM 2.0 naming inconsistency for 3-control X (4 qubits total)
    qasm_str = qasm_str.replace("c4x q[", "c3x q[")
    qc = QuantumCircuit.from_qasm_str(qasm_str)
    res = AerSimulator(seed_simulator=seed).run(qc, shots=shots).result().get_counts()
    return {k.replace(" ", "")[::-1]: int(v) for k, v in res.items()}


# ---------------------------------------------------------------------------------------------- Amazon Braket
def to_braket(c):
    """Braket has no native CRX/CRY/CRZ or 3-control X: decomposed / given as a unitary."""
    from braket.circuits import Circuit
    t = Circuit()
    for op in c["ops"]:
        g, q, v = op["g"], op["q"], _val(op)
        if g == "barrier": continue
        elif g in ("h", "x", "y", "z", "s", "t"): getattr(t, g)(q[0])
        elif g == "sdg": t.si(q[0])
        elif g == "tdg": t.ti(q[0])
        elif g in ("rx", "ry", "rz"): getattr(t, g)(q[0], v)
        elif g == "p": t.phaseshift(q[0], v)
        elif g == "cx": t.cnot(*q)
        elif g == "cy": t.cy(*q)
        elif g == "cz": t.cz(*q)
        elif g == "swap": t.swap(*q)
        elif g == "ccx": t.ccnot(*q)
        elif g == "cp": t.cphaseshift(q[0], q[1], v)
        elif g == "cry":                                   # CRY = cx . ry(-t/2) . cx . ry(t/2) (time order)
            t.cnot(q[0], q[1]); t.ry(q[1], -v / 2); t.cnot(q[0], q[1]); t.ry(q[1], v / 2)
        elif g == "crz":
            t.cnot(q[0], q[1]); t.rz(q[1], -v / 2); t.cnot(q[0], q[1]); t.rz(q[1], v / 2)
        elif g == "crx":                                   # CRX = H . CRZ . H on the target
            t.h(q[1]); t.cnot(q[0], q[1]); t.rz(q[1], -v / 2); t.cnot(q[0], q[1]); t.rz(q[1], v / 2); t.h(q[1])
        elif g == "mcx3":
            m = np.eye(16, dtype=complex); m[[14, 15]] = m[[15, 14]]
            t.unitary(matrix=m, targets=q)
        else: raise ValueError(g)
    return t


def run_braket(c, shots, seed):
    """Local simulator cannot be seeded through run(); the seed is recorded but not enforced."""
    from braket.devices import LocalSimulator
    t = to_braket(c)
    res = LocalSimulator().run(t, shots=shots).result().measurement_counts
    meas = c.get("measure", list(range(c["num_qubits"])))
    out = Counter()
    for k, v in res.items():                  # keys: one char per qubit, qubit 0 first
        out["".join(k[m] for m in meas)] += int(v)
    return dict(out)


# ---------------------------------------------------------------------------------------------- OpenQASM 3
def run_openqasm3(c, shots, seed):
    """Executes the emitted OpenQASM 3 text through qiskit.qasm3 + Aer (needs qiskit_qasm3_import)."""
    from qiskit import qasm3
    from qiskit_aer import AerSimulator
    from qc_ir import to_qasm3
    qc = qasm3.loads(to_qasm3(c))
    res = AerSimulator(seed_simulator=seed).run(qc, shots=shots).result().get_counts()
    return {k.replace(" ", "")[::-1]: int(v) for k, v in res.items()}


RUNNERS = {"qiskit": run_qiskit, "cirq": run_cirq, "pennylane": run_pennylane, "tket": run_tket,
           "braket": run_braket, "openqasm3": run_openqasm3}
