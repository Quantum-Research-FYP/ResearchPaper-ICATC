# Dataset 05: Hardware Execution & Calibration Benchmark

## Overview & Scientific Purpose
This dataset supports **Section IV-B, Section III-E, and Section VI** of the research paper (*"An Integrated Quantum Circuit Learning Platform for Intermediate Learners: Visual Design, Transparent Transpilation, and Real Hardware Execution"*, Paper ID 268).

It directly addresses the critiques of **Reviewer #1, Reviewer #2, and Reviewer #3** regarding physical hardware execution scope, device constraints, and reproducibility.

---

## 1. Distinction Between Supported Capabilities & Physical Executions
In accordance with Reviewer #3's guidance (*"The authors should distinguish the platform's supported execution capability from the experiments actually conducted on physical hardware"*):

1. **Physical Hardware Demonstration (Fig. 2 in Paper):**
   * **Circuit HW02 (Bell State):** Physically executed via IBM Quantum cloud runtime on superconducting hardware (`ibm_brisbane`, Eagle r3 QPU). Observed outcome distribution: $P(|00\rangle) = 0.492$, $P(|11\rangle) = 0.478$, $P(|01\rangle) = 0.015$, $P(|10\rangle) = 0.015$, achieving $D_{\text{TV}} = \frac{1}{2}(|0.492 - 0.5| + |0.478 - 0.5| + |0.015 - 0| + |0.015 - 0|) = \mathbf{0.030}$.
2. **Integrated Execution Capabilities (Platform Drivers):**
   * **IBM Quantum Platform:** Live execution integration via Qiskit Runtime Sampler V2 with automated layout routing and measurement error mitigation.
   * **SpinQ Gemini Mini Pro:** Integrated driver supporting compilation to native NMR pulse rotations ($R_x(\theta), R_y(\theta), R_z(\theta)$) and dispatch via local REST API.
3. **Hardware Boundary Constraint Validation:**
   * **Circuit HW07 (3-Qubit GHZ State):** Evaluated against SpinQ Gemini Mini Pro. The platform transpilation pre-flight check correctly flags this circuit as `UNSUPPORTED` because the target physical NMR hardware possesses only 2 physical qubits.

---

## 2. Experimental Data Files
* **[`metadata/execution_log_experimental.csv`](file:///d:/Datasets/Dataset_05_Experimental_Real_Hardware_Execution/metadata/execution_log_experimental.csv):** Execution records for 7 benchmark circuits (HW01–HW07) across IBM Quantum and SpinQ profiles, with transparent provenance tags (`PHYSICAL_IBM_HARDWARE_DEMONSTRATION` vs `HARDWARE_CALIBRATION_GROUNDED_BENCHMARK`).
* **[`metadata/device_profiles_experimental.csv`](file:///d:/Datasets/Dataset_05_Experimental_Real_Hardware_Execution/metadata/device_profiles_experimental.csv):** Detailed specifications of IBM Eagle r3 (127-qubit Heavy-hex) and SpinQ Gemini Mini Pro (2-qubit NMR desktop system).
* **[`metadata/hardware_execution_tvd_results.csv`](file:///d:/Datasets/Dataset_05_Experimental_Real_Hardware_Execution/metadata/hardware_execution_tvd_results.csv):** Per-execution Total Variation Distance calculations comparing observed probability distributions against ideal statevector simulations.
