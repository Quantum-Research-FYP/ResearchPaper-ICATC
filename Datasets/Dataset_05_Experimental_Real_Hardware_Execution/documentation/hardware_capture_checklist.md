# Hardware Capture & Execution Checklist

- [x] **Confirm physical hardware**: Executed on real physical backends (`ibm_brisbane` superconducting processor and `SpinQ Gemini Mini Pro` NMR hardware), not simulator substitutes.
- [x] **Record device specifications**: Recorded vendor, model, physical qubit count (127 vs 2), connectivity (heavy-hex vs direct scalar coupling), native basis gates, and calibration timestamps.
- [x] **Document physical boundary conditions**: Explicitly recorded that SpinQ Gemini Mini Pro has 2 physical qubits; circuits requiring > 2 qubits (such as HW07 3-qubit GHZ) are marked `UNSUPPORTED_PHYSICAL_QUBIT_LIMIT` rather than substituted with simulator data.
- [x] **Save canonical logical circuits**: All 6 benchmark circuits specified with analytical reference probabilities.
- [x] **Preserve native compilation traces**: Euler angle decompositions ($R_z - \sqrt{X} - R_z$), native RF pulse sequences, and Hadamard conjugation for reverse-direction CNOTs recorded.
- [x] **Record execution run logs**: Provider job IDs, queue times, hardware execution times, and returned shots captured across 3 repetitions.
- [x] **Standardize bitstring conventions**: All measurement distributions mapped to canonical big-endian ordering ($q_0$ leftmost).
- [x] **Calculate empirical Total Variation Distance**: Computed $D_{TV} = \frac{1}{2}\sum_x |P(x)-Q(x)|$ per execution against exact statevectors.
- [x] **Aggregate performance summary**: Generated per-circuit mean, standard deviation, and fidelity estimates.
