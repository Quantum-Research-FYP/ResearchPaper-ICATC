# Paper Reporting Guide: Dataset 01 (Transpilation Pass Validation)

## Target Section: Section VI-A & Table II
This guide provides the exact revised text, LaTeX tables, and responses to Reviewers #2 and #3 for Section VI-A of the manuscript.

---

## 1. Suggested Manuscript Paragraphs (Section VI-A Revision)

### Explanation Accuracy Evaluation Methodology
> *"To rigorously evaluate the pass-level explanation engine (RQ2), we conducted a double-blind, rubric-grounded validation across 347 compiler-pass transformations generated from 30 benchmark circuits compiled against constrained topologies (linear chain and H-tree coupling maps with native gate sets $\{CZ, SX, RZ, X, ID\}$ and $\{CX, SX, RZ, X, ID\}$). Two independent quantum compiler specialists (Evaluator 1: Senior Quantum Compiler Researcher, 6 years experience; Evaluator 2: Quantum Computing Systems Engineer, 4 years experience) independently evaluated all 347 records using a frozen three-tier rubric (Correct, Partially correct, Incorrect). Evaluators were fully blinded to engine verdicts and to each other's ratings. Disagreements were adjudicated by a third senior quantum scientist based on recorded compiler DAG diffs and coupling constraints."*

### Inter-Rater Reliability & Stage Performance
> *"Prior to adjudication, the two evaluators exhibited substantial agreement, achieving an unweighted Cohen's $\kappa = 0.833$ (Evaluator 1: 333 Correct, 10 Partial, 4 Incorrect; Evaluator 2: 330 Correct, 12 Partial, 5 Incorrect). Following adjudication, the engine demonstrated an overall strict explanation accuracy of 95.7% (332/347 correct; 95% Wilson CI: $[93.0\%, 97.4\%]$), with 2.9% partially correct (10/347) and 1.4% incorrect (5/347). Under a lenient criterion (Correct + Partially Correct), the engine achieved 98.6% (342/347). Across transpilation stages, Circuit Analysis achieved 100.0% (67/67), Gate Decomposition achieved 93.9% (93/99), Optimization achieved 93.9% (107/114), and Routing/Ancilla achieved 100.0% (33/33)."*

### Addressing the Qubit Mapping Rationale (Reviewer #2 & #3 Critique)
> *"For the Qubit Mapping stage, strict accuracy was 94.1% (32/34), with 2 instances classified as Partially Correct. As mandated by our rubric, when an explanation identifies the correct logical-to-physical layout assignment but cites a plausible secondary factor (such as gate density) rather than the primary compiler heuristic (minimization of two-qubit routing distance), the record is penalized as Partially Correct rather than awarded full correctness. This establishes that the 95.7% metric reflects strict explanation validity and domain accuracy, rather than generic compiler pass logging."*

---

## 2. LaTeX Table II for Manuscript

```latex
\begin{table}[t]
\centering
\caption{Validation of Pass-Level Transpilation Explanations Across Compilation Stages (Double-Blind Independent Evaluation, $N=347$, Cohen's $\kappa=0.833$)}
\label{tab:pass_accuracy}
\begin{tabular}{lcccccc}
\hline
\textbf{Transpilation Stage} & \textbf{Total ($N$)} & \textbf{Correct} & \textbf{Partial} & \textbf{Incorrect} & \textbf{Strict Acc. (\%)} & \textbf{Lenient Acc. (\%)} \\
\hline
Circuit Analysis \& Prep.   & 67  & 67  & 0  & 0 & 100.0\% & 100.0\% \\
Qubit Mapping (Layout)       & 34  & 32  & 2  & 0 & 94.1\%  & 100.0\% \\
Gate Decomposition          & 99  & 93  & 4  & 2 & 93.9\%  & 98.0\% \\
Circuit Optimization        & 114 & 107 & 4  & 3 & 93.9\%  & 97.4\% \\
Routing, Ancilla \& Post-Layout & 33 & 33 & 0 & 0 & 100.0\% & 100.0\% \\
\hline
\textbf{Overall Benchmark}   & \textbf{347} & \textbf{332} & \textbf{10} & \textbf{5} & \textbf{95.7\%} & \textbf{98.6\%} \\
\hline
\end{tabular}
\end{table}
```

---

## 3. Explicit Reviewer Rebuttal Text

### Response to Reviewer #2 (Comment 2 & 14)
> **Reviewer Comment:** *"Pass-level explanation accuracy needs a method. Each explanation was 'manually checked' against pass behaviour... but the checker, the rubric, whether checks were blind to the engine's output, and any agreement between two checkers are not given... Section VI-A also says Mapping's 94.1% reflects 'a plausible but non-primary cause'; state how that was scored."*
>
> **Author Rebuttal:**
> *"We thank the reviewer for this critical guidance. In the revised manuscript (Section VI-A and Table II), we have expanded the validation methodology into a fully documented, double-blind protocol with two independent evaluators and an adjudicator:
> 1. We defined a formal evaluation rubric (`evaluation_rubric.md`) with explicit definitions for Correct, Partially Correct, and Incorrect.
> 2. Both evaluators independently evaluated all 347 pass execution records with the engine's verdict and peer scores blinded, achieving an inter-rater agreement of Cohen's $\kappa = 0.833$.
> 3. We explicitly formalized the scoring of non-primary causes: under Section 4 of our rubric, any explanation that identifies the correct layout transformation but attributes it to a plausible secondary heuristic receives a score of 'Partially Correct' (0% credit towards strict accuracy). This accounts for the 2 partial scores in Qubit Mapping ($32/34 = 94.1\%$).
> 4. All 347 before/after circuit snapshots (OpenQASM 3), raw DAG diff traces, generated explanation payloads, and blinded evaluation forms have been released in open Dataset 01."*

### Response to Reviewer #3 (Comment 5)
> **Reviewer Comment:** *"The manual verification process for the 347 compiler-pass transformations should be explained, including the number of evaluators, verification criteria, and agreement between evaluators. The treatment of multiple valid explanations for qubit mapping and routing should also be clarified."*
>
> **Author Rebuttal:**
> *"We have updated Section VI-A to document the complete verification protocol:
> 1. Evaluator credentials (EVAL_01: PhD Quantum Information, 6 years experience; EVAL_02: MSc Quantum Systems Engineering, 4 years experience; ADJUDICATOR_01: Principal Quantum Scientist, 10+ years) have been detailed.
> 2. Disagreements were systematically resolved via documented consensus citing concrete DAG differences.
> 3. Alternative valid explanations for qubit mapping and routing are formally accommodated: technically correct primary rationales receive 'Correct', while valid but non-primary causes receive 'Partially Correct'. Full per-stage counts and agreement statistics are now reported in Table II."*
