# Dataset 02: Multi-Framework Quantum Equivalence Data Dictionary

## Overview
This directory contains empirical benchmark data from executing 30 canonical quantum circuits ($E01$ through $E30$) across six leading quantum programming frameworks:
1. **Qiskit** (`qiskit` 1.4.6, `qiskit_aer` 0.17.2)
2. **Cirq** (`cirq-core` 1.3.0)
3. **PennyLane** (`pennylane` 0.38.0)
4. **TKET** (`pytket` 1.23.0 via OpenQASM 2.0 translation on Aer)
5. **Amazon Braket** (`amazon-braket-sdk` 1.98.0, `amazon-braket-default-simulator` 1.28.0)
6. **OpenQASM 3** (`openqasm3` AST parsed into canonical simulation)

Every circuit was simulated with $10,000$ shots per run across three independent random seeds (`seed=11`, `seed=22`, `seed=33`), yielding $30 \times 6 \times 3 = 540$ empirical execution runs.

---

## File Manifest

| File | Description | Records |
| :--- | :--- | :--- |
| `master_circuit_metadata_E01_E30.csv` | Canonical specification of 30 benchmark circuits covering 7 categories | 30 |
| `framework_execution_runs_10000_shots.csv` | Individual empirical runs ($10,000$ shots) with raw counts, distributions, TVD | 540 |
| `tvd_per_circuit_framework.csv` | Aggregated TVD (mean, std, max, threshold pass) per circuit & framework | 180 |
| `tvd_framework_summary.csv` | Global framework summary statistics across all 30 circuits | 6 |
| `reference_distributions.json` | Exact theoretical statevector probability distributions for all circuits | 30 |
| `sampling_noise_thresholds.csv` | Monte Carlo empirical 95th percentile noise thresholds for $N=10,000$ | 30 |
| `source_defect_and_correction_register.csv` | Register of Reviewer 2 defects and exact corrections implemented | 6 |
| `execute_all_framework_runs.py` | Automated reproducible execution script | - |
| `experimental_equivalence_summary.json` | Complete machine-readable results summary | - |

---

## Column Descriptions

### 1. `master_circuit_metadata_E01_E30.csv`
- `circuit_id`: Canonical ID (`E01` to `E30`).
- `name`: Short mnemonic name (e.g., `bell_state`, `qft_3_on_superposition`).
- `category`: Circuit class:
  - `single_qubit_and_rotations`
  - `entanglement_and_states`
  - `algorithms`
  - `variational_and_parameterized`
  - `routing_and_connectivity`
  - `measurement_and_control`
  - `random_and_stress`
- `qubit_count`: Number of simulated qubits ($n \in [1, 5]$).
- `depth`: Logical circuit depth.
- `gate_count`: Total gate operations in canonical representation.
- `gate_diversity`: Comma-separated list of native gate types used.
- `is_parameterized`: Boolean flag (`True`/`False`).
- `parameter_count`: Number of bound parameters (0 if non-parameterized).
- `measurement_pattern`: Measurement regime (`all_qubits`, `partial`, `conditional`).
- `complexity_tier`: Complexity tier (`basic`, `intermediate`, `advanced`).
- `description`: Technical description of logical circuit function.

### 2. `framework_execution_runs_10000_shots.csv`
- `circuit_id`: Canonical ID (`E01` to `E30`).
- `framework`: Framework evaluated (`qiskit`, `cirq`, `pennylane`, `tket`, `braket`, `openqasm3`).
- `run_id`: Unique run identifier ($1$ to $540$).
- `seed`: Random seed for stochastic sampling (`11`, `22`, or `33`).
- `shots_requested`: Requested shots ($10,000$).
- `shots_returned`: Total measured shots recorded ($10,000$).
- `raw_outcome_counts_json`: JSON map of measured computational basis states to raw integer counts (e.g., `{"00": 4980, "11": 5020}`). Qubit ordering is canonical big-endian ($q_0$ is most significant bit).
- `probability_distribution_json`: JSON map of measured frequencies $P(x) = \text{count}(x) / \text{shots}$.
- `tvd`: Total Variation Distance relative to exact theoretical reference distribution:
  $$D_{TV}(P, Q) = \frac{1}{2} \sum_{x \in \{0,1\}^n} |P(x) - Q(x)|$$
- `noise_p95_threshold`: Monte Carlo 95th percentile sampling threshold at $N=10,000$ shots for this circuit's support size.
- `within_sampling_threshold`: Binary indicator (`1` if $D_{TV} \le \text{noise\_threshold}$, `0` otherwise).
- `wall_time_seconds`: Circuit compilation and execution time.
- `error`: Error message if run failed (empty string for all 540 successful runs).
- `provenance`: Set to `EMPIRICAL_EXECUTION_10000_SHOTS`.

### 3. `tvd_per_circuit_framework.csv`
- `circuit_id`: Canonical circuit identifier.
- `framework`: Framework evaluated.
- `runs_count`: Number of executed independent seed runs ($3$).
- `shots_per_run`: $10,000$.
- `mean_tvd`: Sample mean TVD over the 3 runs: $\bar{D}_{TV} = \frac{1}{3} \sum_{i=1}^3 D_{TV, i}$.
- `std_tvd`: Sample standard deviation across seeds.
- `max_tvd`: Maximum TVD observed among the 3 runs.
- `noise_p95_threshold`: 95th percentile sampling noise threshold.
- `passed_threshold`: Binary indicator (`1` if $\bar{D}_{TV} \le \text{noise\_threshold}$, `0` otherwise).
- `provenance`: `EMPIRICAL_EXECUTION_10000_SHOTS`.

### 4. `tvd_framework_summary.csv`
- `framework`: Framework evaluated.
- `total_runs`: Total empirical runs (90 per framework across 30 circuits $\times$ 3 seeds).
- `circuits_tested`: 30.
- `mean_tvd`: Grand mean TVD across all 90 runs.
- `std_tvd`: Standard deviation across all 90 runs.
- `max_tvd`: Maximum observed TVD across any run for this framework.
- `runs_within_sampling_threshold`: Number of runs passing the $95\%$ noise threshold.
- `pass_rate_percent`: Percentage of runs conforming to theoretical sampling limits.
