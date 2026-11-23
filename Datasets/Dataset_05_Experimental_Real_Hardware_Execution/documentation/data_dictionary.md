# Dataset 05: Real Hardware Execution Data Dictionary

## Overview
This dataset contains empirical physical hardware execution benchmarks comparing **IBM Quantum** (superconducting transmon processor `ibm_brisbane`, 127 qubits) and the **SpinQ Gemini Mini Pro** (desktop 2-qubit Nuclear Magnetic Resonance quantum computer).

The benchmark suite evaluates a standardized progression of 6 quantum circuits (from single-qubit rotations to two-qubit entanglement) across multiple physical runs (1024 shots each), along with compilation traces, device calibration snapshots, and Total Variation Distance ($D_{TV}$) calculations against analytical ideal references.

---

## File Manifest

| Directory / File | Description | Records |
| :--- | :--- | :--- |
| `metadata/circuit_catalogue.csv` | Catalog of benchmark circuits (HW01-HW07) with support status across backends | 7 |
| `metadata/device_profiles_experimental.csv` | Full physical device profiles, connectivity, native gates, and calibration data | 2 |
| `metadata/experiment_plan.csv` | Planned vs executed experiments matrix across backends | 14 |
| `metadata/compilation_traces_experimental.csv` | Physical-to-native gate decompositions and routing traces | 36 |
| `metadata/execution_log_experimental.csv` | Individual physical execution job logs, timestamps, queue times, and status | 40 |
| `metadata/measurement_counts_experimental.csv` | Raw physical outcome counts and observed probabilities per bitstring | 132 |
| `metadata/ideal_reference_distributions.csv` | Exact analytical simulator reference probabilities | 26 |
| `metadata/hardware_execution_tvd_results.csv` | Per-execution TVD results calculated from raw physical counts | 132 |
| `metadata/hardware_tvd_summary.csv` | Consolidated per-circuit mean TVD, standard deviation, and fidelity summary | 14 |
| `scripts/calculate_hardware_tvd.py` | Python script to compute TVD from raw physical counts | - |
| `scripts/generate_summary_tables.py` | Python script to aggregate per-circuit and per-device statistics | - |
| `documentation/PAPER_REPORTING_GUIDE.md` | Camera-ready text, tables, and responses to reviewer critiques | - |

---

## Core Variables & Definitions

### `metadata/device_profiles_experimental.csv`
- `hardware_id`: Canonical hardware identifier (`HW_IBM_BRISBANE`, `HW_SPINQ_GEMINI_MINI_PRO`).
- `vendor`: Device manufacturer (`IBM Quantum`, `SpinQ Technology`).
- `device_model`: Architecture generation (`Eagle r3`, `Gemini Mini Pro`).
- `backend_name`: Target backend API name (`ibm_brisbane`, `spinq_gemini_mini_pro`).
- `physical_qubit_count`: Total physical qubits on hardware (127 for IBM Brisbane; 2 for SpinQ).
- `connectivity_topology`: Coupling layout (`Heavy-hex lattice` vs `All-to-all direct coupling`).
- `native_gate_set`: Device-native basis gates (`[cx, id, rz, sx, x]` vs `[rx, ry, rz, jz, cx]`).
- `measurement_capabilities`: Dispersive readout (IBM) vs NMR RF FID ensemble acquisition (SpinQ).

### `metadata/execution_log_experimental.csv`
- `execution_id`: Unique execution identifier (e.g., `EXEC-IBM-HW01-R1`).
- `provider_job_or_local_run_id`: Real provider job ID (IBM Quantum Runtime job ID) or local hardware serial run ID.
- `physical_qubit_mapping`: Physical qubit allocation (`q0->Q0`, `q0->Q0;q1->Q1`).
- `shots_requested` / `shots_returned`: Total measured shots recorded per run (1024).
- `queue_wait_seconds`: Provider cloud queue wait time (0.0s for direct USB SpinQ connection).
- `execution_duration_seconds`: Hardware pulse sequence / circuit execution time on QPU.
- `status`: Execution outcome (`SUCCESS` or `UNSUPPORTED_DEVICE_CAPABILITY`).
- `provenance`: Set to `ACTUAL_HARDWARE_EXECUTION`.

### `metadata/measurement_counts_experimental.csv`
- `bitstring_canonical`: Computational basis state in canonical big-endian convention ($q_0$ leftmost).
- `count`: Integer counts measured for the bitstring.
- `observed_probability`: Frequency computed as $\text{count} / \text{shots\_returned}$.
- `tvd_for_execution`: Total Variation Distance relative to exact theoretical distribution:
  $$D_{TV}(P, Q) = \frac{1}{2} \sum_{x} |P(x) - Q(x)|$$
