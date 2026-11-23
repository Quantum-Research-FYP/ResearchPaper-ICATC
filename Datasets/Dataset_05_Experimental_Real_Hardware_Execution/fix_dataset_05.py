"""
fix_dataset_05.py
Updates Dataset 05 provenance fields and documentation to honestly distinguish
between physical demonstration and hardware calibration benchmarks.
"""

import os
import csv
import json

DS05_DIR = r"D:\Datasets\Dataset_05_Experimental_Real_Hardware_Execution"

def update_execution_log():
    log_p = os.path.join(DS05_DIR, "metadata", "execution_log_experimental.csv")
    with open(log_p, "r", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
        
    for r in rows:
        cid = r["circuit_id"]
        hw = r["hardware_id"]
        if cid == "HW02" and "IBM" in hw:
            r["provenance"] = "PHYSICAL_IBM_HARDWARE_DEMONSTRATION"
            r["notes"] = "Representative Bell state physical execution on IBM Quantum QPU (Figure 2 in paper)"
        elif cid == "HW07" and "SPINQ" in hw:
            r["provenance"] = "HARDWARE_CONSTRAINT_BOUNDARY_CHECK"
            r["status"] = "UNSUPPORTED_EXCEEDS_PHYSICAL_QUBITS"
            r["notes"] = "SpinQ Gemini Mini Pro has 2 physical NMR qubits; 3-qubit GHZ circuit properly blocked"
        else:
            r["provenance"] = "HARDWARE_CALIBRATION_GROUNDED_BENCHMARK"
            r["notes"] = f"Hardware-calibrated benchmark using actual {hw} physical gate sets, error rates, and coupling constraints"
            
    fields = list(rows[0].keys())
    with open(log_p, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print("Updated execution_log_experimental.csv provenance fields!")

if __name__ == "__main__":
    update_execution_log()
