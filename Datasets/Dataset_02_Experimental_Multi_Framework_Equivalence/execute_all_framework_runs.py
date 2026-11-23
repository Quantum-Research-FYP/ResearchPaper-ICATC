"""
execute_all_framework_runs.py
Executes the Multi-Framework Equivalence 10,000-Shot Experiment across all 30 canonical circuits (E01-E30)
and all 6 supported quantum frameworks (Qiskit, Cirq, PennyLane, TKET, Braket, OpenQASM 3).

Protocol:
1. Canonical logical circuit representation (OPENQASM 3.0 / IR JSON)
2. Equivalent measurement mappings and canonical qubit ordering (q0 leftmost)
3. 10,000 shots per run under ideal simulation conditions
4. Multiple independent random seeds (seeds 11, 22, 33)
5. Comparison against exact statevector/analytic reference distribution
6. Total Variation Distance (TVD) calculation: D_TV(P, Q) = 0.5 * sum_x |P(x) - Q(x)|
7. Evaluated against 95th-percentile pure sampling noise threshold
"""

import csv
import json
import math
import os
import sys
import time
import statistics as st
import numpy as np

# Local file paths within this standalone directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CIRCUITS_JSON = os.path.join(BASE_DIR, "circuits_ir.json")
REF_DIST_PATH = os.path.join(BASE_DIR, "reference_distributions.json")
THRESHOLDS_PATH = os.path.join(BASE_DIR, "sampling_noise_thresholds.csv")

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from frameworks import RUNNERS

def tvd(p, q):
    """Computes Total Variation Distance between empirical p and reference q."""
    all_keys = set(p.keys()) | set(q.keys())
    return 0.5 * sum(abs(p.get(k, 0.0) - q.get(k, 0.0)) for k in all_keys)

def main():
    print("="*75)
    print("EXECUTING MULTI-FRAMEWORK EQUIVALENCE STUDY (10,000 SHOTS PER RUN)")
    print("="*75)

    with open(CIRCUITS_JSON, encoding="utf-8") as f:
        circs = json.load(f)

    with open(REF_DIST_PATH, encoding="utf-8") as f:
        ref_data = json.load(f)["distributions"]

    thresholds = {}
    with open(THRESHOLDS_PATH, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            thresholds[(r["circuit_id"], int(r["shots"]))] = float(r["p95_tvd_sample_vs_exact"])

    frameworks = ["qiskit", "cirq", "pennylane", "tket", "braket", "openqasm3"]
    seeds = [11, 22, 33]
    shots = 10000

    raw_runs = []
    run_id = 1
    total_planned = len(circs) * len(frameworks) * len(seeds)
    print(f"Total Circuits: {len(circs)} | Frameworks: {len(frameworks)} | Seeds: {len(seeds)}")
    print(f"Total Execution Runs: {total_planned} | Shots Per Run: {shots:,}")
    print("-"*75)

    start_time = time.time()
    for c_idx, c in enumerate(circs, 1):
        cid = c["id"]
        c_ref = ref_data[cid]
        p95_lim = thresholds.get((cid, shots), 0.010)

        for fw in frameworks:
            for s in seeds:
                t0 = time.time()
                try:
                    counts = RUNNERS[fw](c, shots, s)
                    err = ""
                except Exception as e:
                    counts = {}
                    err = str(e)

                wtime = round(time.time() - t0, 4)
                actual_shots = sum(counts.values())

                if actual_shots > 0:
                    prob_dist = {k: v / actual_shots for k, v in counts.items()}
                    tvd_val = round(tvd(prob_dist, c_ref), 6)
                    passed = int(tvd_val <= p95_lim)
                else:
                    prob_dist = {}
                    tvd_val = None
                    passed = 0

                raw_runs.append({
                    "circuit_id": cid,
                    "framework": fw,
                    "run_id": run_id,
                    "seed": s,
                    "shots_requested": shots,
                    "shots_returned": actual_shots,
                    "raw_outcome_counts_json": json.dumps(counts, sort_keys=True),
                    "probability_distribution_json": json.dumps(prob_dist, sort_keys=True),
                    "tvd": tvd_val,
                    "noise_p95_threshold": round(p95_lim, 6),
                    "within_sampling_threshold": passed,
                    "wall_time_seconds": wtime,
                    "error": err,
                    "provenance": "EMPIRICAL_EXECUTION_10000_SHOTS"
                })
                run_id += 1

        print(f"Completed [{c_idx:02d}/30] Circuit {cid}: {c['name']} across all 6 frameworks.")

    elapsed = round(time.time() - start_time, 2)
    print("-"*75)
    print(f"ALL {len(raw_runs)} RUNS COMPLETED IN {elapsed} SECONDS.")

    # 1. Write framework_execution_runs_10000_shots.csv
    runs_file = "framework_execution_runs_10000_shots.csv"
    with open(runs_file, "w", newline="", encoding="utf-8-sig") as f:
        fieldnames = list(raw_runs[0].keys())
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(raw_runs)
    print(f"Saved: {runs_file}")

    # 2. Aggregate per circuit x framework
    grp = {}
    for r in raw_runs:
        if r["tvd"] is not None:
            grp.setdefault((r["circuit_id"], r["framework"]), []).append(r)

    cf_rows = []
    for (cid, fw), r_list in sorted(grp.items()):
        tvds = [x["tvd"] for x in r_list]
        p95_lim = r_list[0]["noise_p95_threshold"]
        all_passed = int(all(x["within_sampling_threshold"] == 1 for x in r_list))
        cf_rows.append({
            "circuit_id": cid,
            "framework": fw,
            "runs_count": len(tvds),
            "shots_per_run": shots,
            "mean_tvd": round(st.mean(tvds), 6),
            "std_tvd": round(st.stdev(tvds), 6) if len(tvds) > 1 else 0.0,
            "max_tvd": round(max(tvds), 6),
            "noise_p95_threshold": p95_lim,
            "passed_threshold": all_passed,
            "provenance": "EMPIRICAL_EXECUTION_10000_SHOTS"
        })

    cf_file = "tvd_per_circuit_framework.csv"
    with open(cf_file, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(cf_rows[0].keys()))
        writer.writeheader()
        writer.writerows(cf_rows)
    print(f"Saved: {cf_file}")

    # 3. Overall summary per framework
    fw_summary = []
    for fw in frameworks:
        fw_runs = [x for x in raw_runs if x["framework"] == fw and x["tvd"] is not None]
        fw_tvds = [x["tvd"] for x in fw_runs]
        pass_count = sum(x["within_sampling_threshold"] for x in fw_runs)
        pass_rate = (pass_count / len(fw_runs)) * 100.0 if fw_runs else 0.0
        fw_summary.append({
            "framework": fw,
            "total_runs": len(fw_runs),
            "circuits_tested": len(circs),
            "mean_tvd": round(st.mean(fw_tvds), 6),
            "std_tvd": round(st.stdev(fw_tvds), 6),
            "max_tvd": round(max(fw_tvds), 6),
            "runs_within_sampling_threshold": pass_count,
            "pass_rate_percent": round(pass_rate, 2)
        })

    sum_file = "tvd_framework_summary.csv"
    with open(sum_file, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(fw_summary[0].keys()))
        writer.writeheader()
        writer.writerows(fw_summary)
    print(f"Saved: {sum_file}")

    # 4. Export JSON
    overall_all_tvds = [x["tvd"] for x in raw_runs if x["tvd"] is not None]
    json_out = {
        "study": "Multi-Framework Equivalence 10,000-Shot Empirical Execution",
        "provenance": "EMPIRICAL_EXECUTION_10000_SHOTS",
        "total_canonical_circuits": len(circs),
        "frameworks_evaluated": frameworks,
        "shots_per_run": shots,
        "seeds_used": seeds,
        "total_execution_runs": len(raw_runs),
        "overall_mean_tvd": round(st.mean(overall_all_tvds), 6),
        "overall_std_tvd": round(st.stdev(overall_all_tvds), 6),
        "overall_pass_rate_percent": round((sum(x['within_sampling_threshold'] for x in raw_runs) / len(raw_runs)) * 100.0, 2),
        "framework_summaries": fw_summary,
        "per_circuit_summary": cf_rows
    }

    with open("experimental_equivalence_summary.json", "w", encoding="utf-8") as f:
        json.dump(json_out, f, indent=2)
    print("Saved: experimental_equivalence_summary.json")

    print("="*75)
    print("FRAMEWORK SUMMARY RESULTS:")
    print("="*75)
    for r in fw_summary:
        print(f"  {r['framework']:12s} | Runs: {r['total_runs']} | Mean TVD: {r['mean_tvd']:.6f} +/- {r['std_tvd']:.6f} | Pass Rate: {r['pass_rate_percent']}%")
    print("="*75 + "\n")

if __name__ == "__main__":
    main()
