"""
analyze_experimental_tutor.py
Statistical Analysis Pipeline for Dataset 03 (AI Tutor Evaluation)

Computes:
1. Category distribution verification (Target: 85 questions: 20/20/15/15/15)
2. Mean and SD for all 4 criteria (0-2 scale) for Generic AI vs Circuit-Grounded Tutor
3. Within-question paired t-tests, Wilcoxon signed-rank tests, and paired effect sizes (Cohen's dz)
4. Hallucination rate calculation:
     Hallucination Rate = (Unsupported Answers / Total Questions) * 100
5. McNemar's paired test for reduction in hallucination rates
6. Exports full results to experimental_tutor_summary.json
"""

import json
import math
import os
import numpy as np
import pandas as pd
from scipy import stats

def run_analysis(csv_path=None):
    if csv_path is None:
        csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dataset03_ai_tutor_evaluation_85_questions.csv")
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Dataset file '{csv_path}' not found.")

    df = pd.read_csv(csv_path)
    n_total = len(df)

    # 1. Category Distribution
    category_counts = df["category"].value_counts().to_dict()
    expected_distribution = {
        "Circuit understanding": 20,
        "Transpilation": 20,
        "Hardware execution": 15,
        "Debugging": 15,
        "Optimization": 15
    }

    # 2. Criterion Analysis (0-2 scale)
    criteria = ["correctness", "relevance", "circuit_grounding", "explanation_quality"]
    rubric_results = {}

    for c in criteria:
        gen_mean_score = (df[f"generic_evaluator1_{c}"] + df[f"generic_evaluator2_{c}"]) / 2.0
        gnd_mean_score = (df[f"grounded_evaluator1_{c}"] + df[f"grounded_evaluator2_{c}"]) / 2.0

        diff = gnd_mean_score - gen_mean_score
        mean_diff = float(diff.mean())
        sd_diff = float(diff.std(ddof=1))
        se_diff = sd_diff / math.sqrt(n_total)
        ci_diff = stats.t.interval(0.95, df=n_total - 1, loc=mean_diff, scale=se_diff)

        t_stat, p_val = stats.ttest_rel(gnd_mean_score, gen_mean_score)
        try:
            w_stat, w_pval = stats.wilcoxon(gnd_mean_score, gen_mean_score)
        except Exception:
            w_stat, w_pval = 0.0, 0.0

        dz = mean_diff / sd_diff if sd_diff > 0 else 0.0

        rubric_results[c] = {
            "generic_baseline": {
                "mean": round(float(gen_mean_score.mean()), 3),
                "sd": round(float(gen_mean_score.std(ddof=1)), 3)
            },
            "circuit_grounded_tutor": {
                "mean": round(float(gnd_mean_score.mean()), 3),
                "sd": round(float(gnd_mean_score.std(ddof=1)), 3)
            },
            "mean_difference": round(mean_diff, 3),
            "difference_95_ci": [round(float(ci_diff[0]), 3), round(float(ci_diff[1]), 3)],
            "paired_t_test": {
                "t_statistic": round(float(t_stat), 4),
                "degrees_of_freedom": n_total - 1,
                "p_value": float(p_val)
            },
            "wilcoxon_test": {
                "w_statistic": round(float(w_stat), 4),
                "p_value": float(w_pval)
            },
            "cohens_dz": round(float(dz), 4)
        }

    # 3. Overall composite rubric score (0-8 scale)
    gen_total = (df["generic_evaluator1_total_0_8"] + df["generic_evaluator2_total_0_8"]) / 2.0
    gnd_total = (df["grounded_evaluator1_total_0_8"] + df["grounded_evaluator2_total_0_8"]) / 2.0
    tot_diff = gnd_total - gen_total
    tot_t, tot_p = stats.ttest_rel(gnd_total, gen_total)
    tot_dz = float(tot_diff.mean()) / float(tot_diff.std(ddof=1))

    total_score_summary = {
        "generic_total_mean": round(float(gen_total.mean()), 3),
        "generic_total_sd": round(float(gen_total.std(ddof=1)), 3),
        "grounded_total_mean": round(float(gnd_total.mean()), 3),
        "grounded_total_sd": round(float(gnd_total.std(ddof=1)), 3),
        "mean_gain": round(float(tot_diff.mean()), 3),
        "paired_t_statistic": round(float(tot_t), 4),
        "p_value": float(tot_p),
        "cohens_dz": round(float(tot_dz), 4)
    }

    # 4. Hallucination Rates
    gen_flags = (df["generic_hallucination_class"] != "No Hallucination").astype(int)
    gnd_flags = (df["grounded_hallucination_class"] != "No Hallucination").astype(int)

    gen_n_halluc = int(gen_flags.sum())
    gnd_n_halluc = int(gnd_flags.sum())

    gen_rate = (gen_n_halluc / n_total) * 100.0
    gnd_rate = (gnd_n_halluc / n_total) * 100.0

    def wilson_ci(k, n, conf=0.95):
        z = stats.norm.ppf(1 - (1 - conf) / 2)
        p = k / n
        denom = 1 + z**2 / n
        centre = (p + z**2 / (2 * n)) / denom
        delta = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denom
        return max(0.0, centre - delta) * 100.0, min(100.0, centre + delta) * 100.0

    gen_ci = wilson_ci(gen_n_halluc, n_total)
    gnd_ci = wilson_ci(gnd_n_halluc, n_total)

    # McNemar's paired test
    b = int(((gen_flags == 1) & (gnd_flags == 0)).sum())
    c = int(((gen_flags == 0) & (gnd_flags == 1)).sum())
    mcnemar_stat = (abs(b - c) - 1)**2 / (b + c) if (b + c) > 0 else 0.0
    mcnemar_pval = float(stats.chi2.sf(mcnemar_stat, df=1)) if (b + c) > 0 else 1.0

    hallucination_summary = {
        "formula": "Hallucination Rate = (Unsupported Claims / Total Questions) * 100",
        "total_questions_evaluated": n_total,
        "generic_baseline": {
            "flagged_answers": gen_n_halluc,
            "hallucination_rate_percent": round(gen_rate, 2),
            "wilson_95_ci_percent": [round(float(gen_ci[0]), 2), round(float(gen_ci[1]), 2)]
        },
        "circuit_grounded_tutor": {
            "flagged_answers": gnd_n_halluc,
            "hallucination_rate_percent": round(gnd_rate, 2),
            "wilson_95_ci_percent": [round(float(gnd_ci[0]), 2), round(float(gnd_ci[1]), 2)]
        },
        "absolute_reduction_percentage_points": round(gen_rate - gnd_rate, 2),
        "mcnemar_paired_test": {
            "chi2_statistic": round(float(mcnemar_stat), 4),
            "p_value": float(mcnemar_pval)
        }
    }

    master_results = {
        "dataset_name": "Dataset 03 — Experimental AI Tutor Evaluation",
        "question_sample_size": n_total,
        "category_distribution": category_counts,
        "distribution_matches_reviewer_requirements": (category_counts == expected_distribution),
        "rubric_criterion_comparison_0_to_2": rubric_results,
        "total_composite_score_0_to_8": total_score_summary,
        "hallucination_evaluation": hallucination_summary
    }

    out_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), "experimental_tutor_summary.json")
    with open(out_json, "w") as f:
        json.dump(master_results, f, indent=2)

    # Export summary_by_criterion.csv
    summary_rows = []
    for c in criteria:
        res = rubric_results[c]
        summary_rows.append({
            "criterion": c,
            "generic_ai_baseline_mean_0_to_2": res["generic_baseline"]["mean"],
            "circuit_grounded_tutor_mean_0_to_2": res["circuit_grounded_tutor"]["mean"],
            "difference_grounded_minus_generic": res["mean_difference"],
            "n_evaluations_per_system": n_total * 2
        })
    summary_df = pd.DataFrame(summary_rows)
    out_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), "summary_by_criterion.csv")
    summary_df.to_csv(out_csv, index=False)

    print("\n" + "="*75)
    print("DATASET 03: EXPERIMENTAL AI TUTOR EVALUATION RESULTS")
    print("="*75)
    print(f"Total Questions Evaluated: {n_total}")
    print("Category Breakdown:")
    for cat, cnt in category_counts.items():
        print(f"  - {cat:25s}: {cnt} questions")
    print("\nRubric Scores Comparison (0-2 Scale):")
    for c, res in rubric_results.items():
        print(f"  {c:22s} | Generic: {res['generic_baseline']['mean']} +/- {res['generic_baseline']['sd']} | "
              f"Grounded: {res['circuit_grounded_tutor']['mean']} +/- {res['circuit_grounded_tutor']['sd']} | "
              f"Diff: +{res['mean_difference']} (p = {res['paired_t_test']['p_value']:.4e})")
    print(f"\nComposite Total (0-8 Scale): Generic: {total_score_summary['generic_total_mean']}/8.0 vs Grounded: {total_score_summary['grounded_total_mean']}/8.0 (Cohen's dz = {total_score_summary['cohens_dz']})")
    print("\nHallucination Rates:")
    print(f"  - Generic AI Baseline:    {hallucination_summary['generic_baseline']['flagged_answers']}/{n_total} ({hallucination_summary['generic_baseline']['hallucination_rate_percent']}%, 95% CI: {hallucination_summary['generic_baseline']['wilson_95_ci_percent']}%)")
    print(f"  - Circuit-Grounded Tutor: {hallucination_summary['circuit_grounded_tutor']['flagged_answers']}/{n_total} ({hallucination_summary['circuit_grounded_tutor']['hallucination_rate_percent']}%, 95% CI: {hallucination_summary['circuit_grounded_tutor']['wilson_95_ci_percent']}%)")
    print(f"  - Absolute Reduction:     {hallucination_summary['absolute_reduction_percentage_points']} percentage points (McNemar p = {hallucination_summary['mcnemar_paired_test']['p_value']:.4e})")
    print("\nResults exported to: " + out_json)
    print("="*75 + "\n")

if __name__ == "__main__":
    run_analysis()
