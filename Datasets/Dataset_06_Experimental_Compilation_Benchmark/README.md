# Dataset 06: Compilation Benchmark (Experimental Release)

This directory contains the empirical quantum circuit compilation benchmark and transparency instrumentation evaluation comparing:
1. **Qiskit Default (Level 1)**: Industry baseline preset pass manager (`optimization_level=1`).
2. **Qiskit Default (Level 3)**: High-effort optimization pipeline (`optimization_level=3`).
3. **PyTKET Default**: Industrial compiler sequence (`FullPeepholeOptimise`, `DefaultMappingPass`).
4. **Quantum Studio Transparent Compiler (`platform_instrumented`)**: Qiskit Level 1 equipped with event-driven DAG pass-logging instrumentation.

---

## Benchmark Design & Protocol

- **Circuits:** 40 canonical quantum circuits (`T01` to `T40`) covering single-qubit rotations, entanglement, Clifford circuits, swap chains, and multi-controlled operations.
- **Backends:** Evaluated across two constrained target topologies:
  - `linear_6`: 6-qubit linear nearest-neighbor coupling.
  - `h_shape_7`: 7-qubit H-shaped branching topology.
- **Basis Gate Set:** $\{cx, id, rz, sx, x\}$.
- **Timing Protocol:** 1 untimed warm-up iteration followed by **10 independent timed repetitions** (reporting median latency).
- **Total Empirical Runs:** $40 \text{ circuits} \times 2 \text{ backends} \times 4 \text{ compilers} = 320$ benchmark entries.

---

## Reviewer 2 & Report Criteria Satisfied

1. **Routing Overhead Formula Corrected:**
   - Conventional ratio: $R = \frac{G_{\text{after}} - G_{\text{before}}}{G_{\text{before}}}$
   - Isolating Multi-Qubit Metric: $\Delta Q = Q_{\text{after}} - Q_{\text{before}}$ (measuring added two-qubit operations and SWAPs without confounding from single-qubit Euler basis translations).
2. **Test A (Output Identity):**
   - Verified that Quantum Studio's instrumented transpiler produces bit-for-bit identical circuits to plain Qiskit Level 1 with 0 divergence in gate counts, depth, or 2Q gates (`same_output_as_plain_qiskit = TRUE_IDENTICAL_OUTPUT`).
3. **Test B (Transparency Instrumentation Overhead):**
   - Directly quantified $T_{\text{overhead}} = T_{\text{platform}} - T_{\text{plain\_qiskit}}$ (mean latency overhead is nominal: $\sim 0.5 - 2.5\text{ ms}$).
4. **Functional Equivalence:**
   - $100.0\%$ of compiled circuits validated via statevector/operator fidelity under final qubit layout permutations ($F \ge 0.999999$).

---

## Directory Structure

- `metadata/`
  - `circuit_catalogue_40_circuits.csv`: Logical input circuit specifications and pre-compilation metrics.
  - `target_configurations.csv`: Coupling maps and basis gates for `linear_6` and `h_shape_7`.
  - `compilation_benchmark_320_runs.csv`: Complete empirical results across all 320 compiler runs.
  - `instrumentation_overhead_evaluation.csv`: Detailed Test A and Test B evaluation comparing plain Qiskit to Quantum Studio.
  - `compiler_comparison_summary.csv`: Aggregated paired summary metrics per compiler and backend.
- `scripts/`
  - `run_compilation_benchmark.py`: Standalone execution pipeline script.
  - `frameworks.py`, `qc_ir.py`: Standalone translation utilities.
- `documentation/`
  - `DATA_DICTIONARY.md`: Complete variable and schema documentation.
  - `benchmark_checklist.md`: Audit checklist fulfilling reviewer requirements.
  - `PAPER_REPORTING_GUIDE.md`: Camera-ready manuscript text, summary tables, and reviewer rebuttal points.

---

## Reproducing the Benchmark

To re-execute all 320 benchmark runs from scratch:
```powershell
cd scripts
python run_compilation_benchmark.py
```
