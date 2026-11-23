# Dataset 06: Quantum Circuit Compilation Benchmark Data Dictionary

## Overview
This dataset contains empirical compilation and transpilation benchmark records comparing:
1. **Qiskit Default (Level 1)**: Industry-standard fast heuristic compiler (`optimization_level=1`).
2. **Qiskit Default (Level 3)**: High-effort optimization pipeline (`optimization_level=3`) using advanced routing (SabreSwap) and Peephole synthesis.
3. **PyTKET Default**: Industrial quantum compiler pipeline (`SequencePass` with rebase, `FullPeepholeOptimise`, `DefaultMappingPass`).
4. **Quantum Studio Transparent Compiler (`platform_instrumented`)**: Quantum Studio transpilation engine executing level-1 optimization while capturing pass-by-pass DAG transformations, graph metrics, and visual telemetry.

The benchmark evaluates **40 canonical quantum circuits** (`T01` to `T40`) across **2 target coupling topologies** (`linear_6` and `h_shape_7`), yielding $40 \times 2 \times 4 = 320$ empirical benchmark entries.

Each benchmark execution incorporates a warm-up compilation run followed by **10 timed iterations** to establish statistically robust median compilation latencies.

---

## File Manifest

| File | Description | Records |
| :--- | :--- | :--- |
| `metadata/circuit_catalogue_40_circuits.csv` | Full specification and pre-compilation metrics for all 40 canonical benchmark circuits | 40 |
| `metadata/target_configurations.csv` | Coupling maps, topologies, and native basis gates for `linear_6` and `h_shape_7` | 2 |
| `metadata/compilation_benchmark_320_runs.csv` | Master empirical benchmark dataset recording pre/post metrics, routing, timings, and equivalence | 320 |
| `metadata/instrumentation_overhead_evaluation.csv` | Reviewer-mandated Test A (output identity) and Test B (overhead latency) evaluations | 80 |
| `metadata/compiler_comparison_summary.csv` | Paired compiler summary table aggregated by backend architecture | 8 |
| `scripts/run_compilation_benchmark.py` | Automated benchmark execution suite | - |
| `documentation/PAPER_REPORTING_GUIDE.md` | Camera-ready manuscript text, tables, formulas, and reviewer rebuttal points | - |
| `documentation/benchmark_checklist.md` | Audit verification checklist fulfilling reviewer instructions | - |

---

## Column Descriptions

### `metadata/compilation_benchmark_320_runs.csv`
- `benchmark_id`: Unique identifier formatted as `BENCH-{circuit_id}-{backend}-{compiler}`.
- `circuit_id`: Canonical circuit identifier (`T01` through `T40`).
- `circuit_name`: Descriptive name of circuit function.
- `backend`: Target device topology (`linear_6` or `h_shape_7`).
- `compiler`: Compiler under evaluation (`qiskit_default_o1`, `qiskit_default_o3`, `pytket_default`, `platform_instrumented`).
- `logical_gates_before`: Input circuit operation count ($G_{\text{before}}$).
- `logical_depth_before`: Input circuit critical path depth.
- `logical_multiqubit_before`: Input circuit multi-qubit entangling gate count ($Q_{\text{before}}$).
- `gates_after`: Compiled circuit total operation count ($G_{\text{after}}$).
- `depth_after`: Compiled circuit critical path depth.
- `two_qubit_gates_after`: Compiled circuit two-qubit gate count ($Q_{\text{after}}$).
- `swaps_or_added_2q_gates`: Reviewer-mandated clean routing measure:
  $$\Delta Q = Q_{\text{after}} - Q_{\text{before}}$$
  (explicitly isolating routing and swap insertions from single-qubit basis translations).
- `routing_overhead_R`: Relative gate increase ratio:
  $$R = \frac{G_{\text{after}} - G_{\text{before}}}{G_{\text{before}}}$$
- `compile_time_median_s`: Median compilation wall-clock duration over 10 iterations after warm-up (in seconds).
- `compile_time_median_ms`: Median compilation latency in milliseconds.
- `compile_time_runs`: Number of timed iterations collected ($10$).
- `functionally_equivalent`: Validation flag (`VALIDATED_TRUE` if compiled unitary/statevector matches logical input under layout permutation).
- `equivalence_method`: Formal verification procedure applied (`Statevector/Operator fidelity under layout permutation (F >= 0.999999)`).
- `compiler_version`: Exact software package version.
- `optimization_setting`: Transpiler pass-manager settings.
- `seed`: Random seed for stochastic layout and routing passes ($1234$).
- `same_output_as_plain_qiskit`: Test A validation result (`TRUE_IDENTICAL_OUTPUT` for Quantum Studio platform vs plain Qiskit Level 1).
- `instrumentation_overhead_ms`: Test B measured time overhead:
  $$T_{\text{overhead}} = T_{\text{platform}} - T_{\text{plain\_qiskit}}$$
- `provenance`: Recorded as `EMPIRICAL_COMPILATION_BENCHMARK`.

---

### `metadata/instrumentation_overhead_evaluation.csv`
- Evaluates the core claim: *"Quantum Studio provides additional transparency without compromising compilation correctness or behaviour."*
- Directly compares paired runs between `platform_instrumented` and `qiskit_default_o1` across all 40 circuits and both backends:
  - **Test A:** Compares gate sequence, gate counts, depth, and two-qubit operations.
  - **Test B:** Quantifies latency cost of pass instrumentation ($T_{\text{overhead}} \text{ ms}$ and overhead percentage).
