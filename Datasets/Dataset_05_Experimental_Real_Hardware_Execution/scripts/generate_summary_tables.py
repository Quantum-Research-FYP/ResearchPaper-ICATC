import csv
import json
import statistics as st
from collections import defaultdict

tvd_file = r"D:\Dataset_04_Synthetic_Controlled_Study_Complete\Dataset_05_Experimental_Real_Hardware_Execution\metadata\hardware_execution_tvd_results.csv"

# Load execution-level TVD
exec_tvd = {}
with open(tvd_file, encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        k = (r["hardware_id"], r["circuit_id"], r["execution_id"])
        exec_tvd[k] = float(r["tvd_for_execution"])

# Group by (hardware_id, circuit_id)
grouped = defaultdict(list)
for (hid, cid, eid), val in exec_tvd.items():
    grouped[(hid, cid)].append(val)

circuit_names = {
    "HW01": "Single-qubit superposition (H)",
    "HW02": "Single-qubit rotation (Ry)",
    "HW03": "Computational-basis control (X)",
    "HW04": "Bell state (H+CX)",
    "HW05": "Reverse-direction entanglement",
    "HW06": "Rotation + entanglement (Ry+CX)",
    "HW07": "Three-qubit GHZ state"
}

summary_rows = []
for (hid, cid), tvds in sorted(grouped.items()):
    mean_tvd = st.mean(tvds)
    std_tvd = st.stdev(tvds) if len(tvds) > 1 else 0.0
    summary_rows.append({
        "hardware_id": hid,
        "platform": "IBM Quantum (ibm_brisbane)" if "IBM" in hid else "SpinQ Gemini Mini Pro",
        "circuit_id": cid,
        "circuit_name": circuit_names.get(cid, cid),
        "executions_count": len(tvds),
        "mean_tvd": round(mean_tvd, 6),
        "std_tvd": round(std_tvd, 6),
        "min_tvd": round(min(tvds), 6),
        "max_tvd": round(max(tvds), 6),
        "hardware_fidelity_estimate": round(1.0 - mean_tvd, 6),
        "status": "VALIDATED_PHYSICAL_EXECUTION"
    })

# Add the explicitly unsupported entry for SpinQ on HW07
summary_rows.append({
    "hardware_id": "HW_SPINQ_GEMINI_MINI_PRO",
    "platform": "SpinQ Gemini Mini Pro",
    "circuit_id": "HW07",
    "circuit_name": circuit_names["HW07"],
    "executions_count": 0,
    "mean_tvd": "",
    "std_tvd": "",
    "min_tvd": "",
    "max_tvd": "",
    "hardware_fidelity_estimate": "",
    "status": "UNSUPPORTED_PHYSICAL_QUBIT_LIMIT (Max 2 qubits)"
})

out_csv = r"D:\Dataset_04_Synthetic_Controlled_Study_Complete\Dataset_05_Experimental_Real_Hardware_Execution\metadata\hardware_tvd_summary.csv"
with open(out_csv, "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(summary_rows[0].keys()))
    w.writeheader()
    w.writerows(summary_rows)

print("Saved hardware_tvd_summary.csv with", len(summary_rows), "records.")
