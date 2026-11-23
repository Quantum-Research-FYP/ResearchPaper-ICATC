# Dataset 02: Multi-Framework Quantum Equivalence Benchmark (Experimental Release)

This directory contains the complete empirical dataset and reproduction pipeline for evaluating semantic and distributional equivalence across six major quantum computing software frameworks:
- **Qiskit** (`v1.4.6`)
- **Cirq** (`v1.3.0`)
- **PennyLane** (`v0.38.0`)
- **TKET** (`v1.23.0`)
- **Amazon Braket** (`v1.98.0`)
- **OpenQASM 3** (native AST)

---

## Benchmark Structure

- **Circuits:** 30 canonical circuits ($E01$ to $E30$) covering single-qubit gates, entanglement, algorithms, variational forms, swap chains, multi-controlled gates, and random stress circuits.
- **Runs:** 540 empirical runs ($30 \text{ circuits} \times 6 \text{ frameworks} \times 3 \text{ seeds}$).
- **Shot Budget:** $10,000$ shots per run ($5.4 \times 10^6$ total shots).
- **Metric:** Total Variation Distance ($D_{TV}$) between empirical probability distributions and exact analytical statevector references:
  $$D_{TV}(P, Q) = \frac{1}{2}\sum_x |P(x) - Q(x)|$$
- **Overall Result:** Mean $D_{TV} = 0.003857 \pm 0.003725$ (Pass rate: $97.59\%$ against empirical $95\%$ Monte Carlo noise threshold).

---

## File Directory

- `framework_execution_runs_10000_shots.csv`: 540 rows of raw empirical measurements, counts JSON, probabilities, wall times, and individual TVDs.
- `tvd_per_circuit_framework.csv`: 180 rows showing aggregated mean TVD, standard deviation, and threshold status per circuit/framework pair.
- `tvd_framework_summary.csv`: Summary statistics per framework.
- `master_circuit_metadata_E01_E30.csv`: Full metadata for all 30 benchmark circuits.
- `reference_distributions.json`: Exact mathematical probability distributions for all circuits.
- `sampling_noise_thresholds.csv`: Theoretical 95th percentile noise limits for 10,000 shots.
- `source_defect_and_correction_register.csv`: Audit log addressing Reviewer 2 comments.
- `execute_all_framework_runs.py`: End-to-end Python script to re-execute the 540 runs.
- `experimental_equivalence_summary.json`: JSON output containing the complete empirical results.
- `DATA_DICTIONARY.md`: Precise schema definitions for all variables.
- `PAPER_REPORTING_GUIDE.md`: Text, LaTeX equations, and summary tables ready for camera-ready submission.

---

## Reproducing the Benchmark

To re-run the entire benchmark from scratch:
```powershell
python execute_all_framework_runs.py
```
This will re-execute all 540 runs across the 6 installed engines and recompute TVD values against `reference_distributions.json`.
