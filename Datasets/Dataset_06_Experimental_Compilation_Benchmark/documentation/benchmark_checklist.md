# Dataset 06 Benchmark Verification Checklist

This checklist tracks complete fulfillment of all reviewer requirements specified in the peer review report for Dataset 06:

- [x] **Fix routing overhead formula**: Added `swaps_or_added_2q_gates = two_qubit_gates_after - logical_multiqubit_before` alongside $R = (G_{after} - G_{before}) / G_{before}$ to ensure basis translation does not artificially skew routing measurements.
- [x] **Record added two-qubit operations and SWAPs**: Explicitly tabulated for every circuit and compiler run.
- [x] **At least 10 compilation runs after warm-up**: Each benchmark entry executes 1 initial warm-up run followed by 10 independent timed repetitions; median wall-clock time is reported.
- [x] **Functional equivalence check**: Statevector / operator fidelity under final qubit layout permutations verified ($F \ge 0.999999$) across all 320 runs.
- [x] **Identical circuits and basis gates**: All compilers benchmarked against the identical 40 canonical IR circuits (`T01-T40`) and native basis `{cx, id, rz, sx, x}`.
- [x] **Identical target coupling topologies**: Benchmarked across standard `linear_6` (line) and `h_shape_7` (H-shaped branching) topologies.
- [x] **Comparable optimization levels**: Explicitly contrasts Qiskit Level 1, Qiskit Level 3, PyTKET Default, and Quantum Studio Transparent Compiler.
- [x] **Per-circuit individual reporting**: Full 320-run breakdown documented in `compilation_benchmark_320_runs.csv` without hiding under aggregate averages.
- [x] **Test A (Output Identity)**: Confirmed that Quantum Studio's instrumented transpiler produces bit-for-bit identical compiled circuits to plain Qiskit Level 1 (`same_output_as_plain_qiskit = TRUE_IDENTICAL_OUTPUT`).
- [x] **Test B (Instrumentation Latency Overhead)**: Quantified $T_{overhead} = T_{instrumented} - T_{normal}$ across all 40 circuits on both backends.
