# Dataset 03 — Experimental AI Tutor Evaluation

## Package Overview
This package contains the complete empirical evaluation dataset, rubric scores, hallucination assessments, and statistical pipelines for the comparative evaluation of the **Circuit-Grounded Quantum Tutor** against a **Generic LLM Baseline (GPT-4o)** across 85 standardized educational questions.

---

## Files in this Package
1. **`dataset03_ai_tutor_evaluation_85_questions.csv`**:
   The primary experimental dataset ($N=85$ rows) containing question IDs, category, supplied circuit context, ground-truth reference facts, generic LLM output, grounded tutor output, independent 0–2 rubric scores from Evaluators 1 & 2 across all 4 criteria, hallucination classifications, and blinded review orders.
2. **`summary_by_criterion.csv`**:
   Descriptive summary table showing mean scores and differences per rubric criterion.
3. **`category_distribution.csv`**:
   Distribution of the 85 benchmark questions across the five technical domains (20, 20, 15, 15, 15).
4. **`tutor_responses_DATA_ENTRY_TEMPLATE.csv`**:
   Formatted CSV template for logging new evaluation runs or model iterations.
5. **`analyze_experimental_tutor.py`**:
   Automated Python pipeline calculating paired $t$-tests, Wilcoxon signed-rank tests, Cohen's $d_z$ effect sizes, hallucination rates, Wilson 95% confidence intervals, and McNemar's paired test.
6. **`experimental_tutor_summary.json`**:
   Machine-readable export of all descriptive and inferential statistics.
7. **`DATA_DICTIONARY.md`**:
   Detailed variable glossary, data types, and coding standards.
8. **`EVALUATION_RUBRIC.md`**:
   Comprehensive description of the 0–2 rubric, formal hallucination operationalization, and blinding protocol.
9. **`PAPER_REPORTING_GUIDE.md`**:
   Ready-to-use LaTeX tables, reporting prose, and direct reviewer response paragraphs.
10. **`manifest.json`**:
    Package metadata and inventory.

---

## Quick Start: Running the Analysis
To replicate the full statistical analysis and verify all numbers:
```bash
python analyze_experimental_tutor.py
```
