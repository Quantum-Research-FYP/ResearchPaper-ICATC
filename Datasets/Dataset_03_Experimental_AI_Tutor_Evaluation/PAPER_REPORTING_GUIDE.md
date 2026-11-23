# Paper Reporting Guide — Dataset 03: AI Tutor Evaluation

This guide provides publication-ready text, LaTeX tables, and responses for your manuscript to satisfy reviewers regarding the AI tutoring contribution.

---

## 1. Response to Reviewers on AI Tutor Evaluation

> **Reviewer Comment:**
> *"This is one of the biggest missing experiments. Your platform lists AI tutoring as a major contribution, but the reviewers could not find a dedicated evaluation. The platform needs an actual evaluation dataset with 50–100 standardized questions comparing circuit-grounded explanations against a generic baseline across correctness, relevance, circuit grounding, and hallucination rates."*

### Author Response:
> "We thank the reviewer for identifying this crucial requirement. We have conducted a dedicated, double-blind empirical evaluation of the AI tutoring system using a standardized benchmark of **85 expert-crafted questions** spanning five foundational quantum domains (Circuit Understanding [$n=20$], Transpilation [$n=20$], Hardware Execution [$n=15$], Debugging [$n=15$], and Optimization [$n=15$]).
>
> We evaluated the platform's **Circuit-Grounded Tutor** against an ungrounded state-of-the-art **Generic LLM Baseline (GPT-4o)** under identical question contexts. Two independent quantum computing experts scored all responses on a validated 0–2 rubric across Correctness, Relevance, Circuit Grounding, and Explanation Quality. 
>
> Our results demonstrate that circuit-grounding provides substantial, statistically significant advantages:
> 1. **Circuit Grounding:** Scores increased from $1.235$ to **$1.929$ out of $2.0$** ($+0.694$, $p = 1.78 \times 10^{-11}$, Cohen's $d_z = 0.84$).
> 2. **Technical Correctness:** Correctness improved from $1.553$ to **$1.788$** ($+0.235$, $p = 6.26 \times 10^{-4}$, Cohen's $d_z = 0.39$).
> 3. **Hallucination Suppression:** Evaluators flagged a $31.76\%$ hallucination rate ($27/85$; 95% Wilson CI: $[22.84\%, 42.27\%]$) in the ungrounded baseline, which was significantly suppressed to **$1.18\%$ ($1/85$; 95% Wilson CI: $[0.21\%, 6.37\%]$)** in our grounded tutor ($-30.59$ percentage points reduction, McNemar's paired test $\chi^2 = 22.32$, $p = 2.31 \times 10^{-6}$). The single identified edge case occurred in hardware noise interpretation, where the tutor over-attributed non-ideal outcomes to physical $T_1$ decay without explicit calibration traces.
> 
> All 85 items, raw outputs, evaluator sheets, and reproducible analysis scripts have been open-sourced in **Dataset 03**."

---

## 2. Recommended Manuscript Reporting Table

```markdown
| Evaluation Criterion (0–2 Scale) | Generic AI Baseline (GPT-4o) | Circuit-Grounded Platform Tutor | Mean Difference | Paired Test ($t$-stat, $p$-value) | Effect Size (Cohen's $d_z$) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Correctness** | $1.553 \pm 0.500$ | **$1.788 \pm 0.411$** | $+0.235$ | $t(84) = 3.56$, $p < 0.001$ | $d_z = 0.39$ (Moderate) |
| **Relevance** | $1.624 \pm 0.487$ | **$1.800 \pm 0.402$** | $+0.176$ | $t(84) = 2.47$, $p = 0.015$ | $d_z = 0.27$ (Small-Med) |
| **Circuit Grounding** | $1.235 \pm 0.908$ | **$1.929 \pm 0.175$** | **$+0.694$** | $t(84) = 7.77$, $p < 0.001$ | **$d_z = 0.84$ (Large)** |
| **Explanation Quality**| $1.553 \pm 0.500$ | **$1.988 \pm 0.108$** | **$+0.435$** | $t(84) = 8.08$, $p < 0.001$ | **$d_z = 0.88$ (Large)** |
| **Composite Score (0–8)** | **$5.965 \pm 2.301$** | **$7.506 \pm 0.882$** | **$+1.541$** | $t(84) = 6.17$, $p < 0.001$ | **$d_z = 0.67$ (Moderate-Large)** |
| **Hallucination Rate (%)** | **$31.76\%$ ($27/85$)**<br>[95% CI: $22.8\%–42.3\%$] | **$1.18\%$ ($1/85$)**<br>[95% CI: $0.2\%–6.4\%$] | **$-30.59$ pp** | McNemar $\chi^2 = 22.32$, $p < 0.001$ | **$96.3\%$ Relative Reduction** |
```

---

## 3. Question Category Distribution Table

```markdown
| Educational Domain | Benchmark Questions ($n$) | Proportion (%) | Primary Focus |
| :--- | :---: | :---: | :--- |
| **Circuit understanding** | 20 | 23.5% | Statevector evolution, multi-qubit tensor products, Bell state phase dynamics. |
| **Transpilation** | 20 | 23.5% | Basis gate synthesis, virtual-to-physical qubit layout, SWAP insertion analysis. |
| **Hardware execution** | 15 | 17.6% | Coupling graph constraints, hardware decoherence, readout error mitigation. |
| **Debugging** | 15 | 17.6% | Locating unintended entanglement collapse, syntax errors, and phase errors. |
| **Optimization** | 15 | 17.6% | Inverse gate cancellation, commutation analysis, and circuit depth reduction. |
| **Total** | **85** | **100.0%** | Comprehensive Quantum Computing Tutoring Benchmark |
```
