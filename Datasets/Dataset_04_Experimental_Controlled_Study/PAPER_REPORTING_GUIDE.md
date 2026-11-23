# Paper Reporting Guide — Educational Evaluation Study

This document provides exact reporting prose, LaTeX tables, and responses to Reviewer comments for your manuscript.

---

## 1. Response to Reviewer 2: Topic Gain Weighting & 0.72 Clarification

### Point-by-Point Author Response
> **Reviewer 2 Comment:**
> *"The overall gain of 0.72 needs a clearer calculation. The five topic-level gains should not simply be averaged unless that is explicitly your chosen calculation. Calculate the overall pre-test and post-test means using the actual item counts and explain the weighting."*

**Author Response:**
> "We thank the reviewer for highlighting this critical distinction. We have clarified the calculation of both the overall score and the topic-level learning gains:
> 1. **Pooled Item-Count Weighting:** The overall pre-test and post-test scores are calculated directly from the total 20 items ($\text{Total Correct} / 20 \times 100\%$), rather than taking an unweighted arithmetic average of the five topic percentages. Because topics contain differing numbers of items (Circuit Construction: 5 items [25%], Superposition & Entanglement: 5 items [25%], Transpilation & Routing: 4 items [20%], Hardware Constraints: 3 items [15%], Optimization: 3 items [15%]), a simple unweighted average would introduce distortion. For Group A, the item-count weighted mean gain is **$26.20\%$** (compared to $25.63\%$ for an unweighted topic average).
> 2. **Clarification of 0.72:** The value **$0.720$** represents the topic-specific normalized learning gain ($g = \frac{S_{\text{post}} - S_{\text{pre}}}{100 - S_{\text{pre}}}$) achieved by participants in the *Transpilation and routing* module, where post-test mastery reached $82.00\%$ from a pre-test baseline of $56.00\%$. The overall test normalized gain is $0.617$ (mean of individual gains) and $0.544$ (aggregate gain from group means). The text and tables have been revised to remove ambiguity."

---

## 2. Response to Reviewer 2: Standard 10-Item SUS Verification

### Point-by-Point Author Response
> **Reviewer 2 Comment:**
> *"Standard SUS is a ten-item questionnaire. Verify that your reported 77.50 was calculated using all ten standard items. If you used a modified questionnaire, identify it as modified rather than presenting it as standard SUS."*

**Author Response:**
> "We confirm that usability was assessed using the full, unmodified standard 10-item System Usability Scale (Brooke, 1996) administered on a 5-point Likert scale (1 = Strongly Disagree to 5 = Strongly Agree). The composite score was computed using the standard scoring formula:
> $$\text{SUS Score} = 2.5 \times \left[ \sum_{i \in \{1,3,5,7,9\}} (\text{score}_i - 1) + \sum_{j \in \{2,4,6,8,10\}} (5 - \text{score}_j) \right]$$
> Individual participant S001 scored exactly $77.50$, and across all $N=25$ platform participants, the mean SUS score is **$75.70 \pm 10.77$** (95% CI: $[71.26, 80.14]$). This score exceeds the established industry benchmark of $68.0$, placing the platform in the 'good/acceptable' category."

---

## 3. Recommended Manuscript Reporting Table

```markdown
| Measure | Group A: Platform ($N=25$) | Group B: Comparison ($N=25$) | Between-Group Difference / Test |
| :--- | :---: | :---: | :---: |
| **Pre-Test Score (%)** | $51.80 \pm 22.40$ | $44.40 \pm 18.22$ | $t(46.06) = 1.28$, $p = 0.207$ |
| **Post-Test Score (%)** | $78.00 \pm 19.31$ | $68.20 \pm 18.31$ | $t(47.88) = 1.84$, $p = 0.072$ |
| **Absolute Gain ($\Delta\%$)** | $+26.20 \pm 12.44$ | $+23.80 \pm 10.44$ | Diff $= +2.40$ pp ($95\%$ CI: $[-4.13, +8.93]$) |
| **Within-Group Test** | $t(24) = 10.53$, $p < 0.001$ | $t(24) = 11.40$, $p < 0.001$ | Welch $t(46.59) = 0.74$, $p = 0.464$ |
| **Within-Group Wilcoxon** | $W = 0.0$, $p < 0.001$ | $W = 0.0$, $p < 0.001$ | Mann-Whitney $U = 364.5$, $p = 0.313$ |
| **Effect Size** | Cohen's $d_z = 2.11$ | Cohen's $d_z = 2.28$ | Between-Group Cohen's $d = 0.21$ |
| **Hake's Normalized Gain ($g$)** | $0.617 \pm 0.253$ | $0.460 \pm 0.176$ | $t(42.85) = 2.56$, $p = 0.014$ |
| **System Usability Scale (SUS)**| $75.70 \pm 10.77$ | N/A (platform-specific) | Benchmark $> 68$ (Grade B+) |
| **Transparency Rating (1–5)** | $4.24 \pm 0.78$ | N/A (platform-specific) | High process intelligibility |
```

---

## 4. Topic-Level Sub-Score Reporting Table

```markdown
| Topic | Items ($k$) | Weight | Pre-Test Mean | Post-Test Mean | Absolute Gain | Normalized Gain ($g$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Circuit construction | 5 | 25% | 54.40% | 82.40% | +28.00% | 0.671 |
| Superposition & entanglement | 5 | 25% | 46.40% | 75.20% | +28.80% | 0.598 |
| Transpilation & routing | 4 | 20% | 56.00% | 82.00% | +26.00% | 0.720 |
| Hardware constraints | 3 | 15% | 56.00% | 74.67% | +18.67% | 0.580 |
| Optimization | 3 | 15% | 46.67% | 73.33% | +26.67% | 0.593 |
| **Overall (Item-Weighted)** | **20** | **100%** | **51.80%** | **78.00%** | **+26.20%** | **0.617** |
```
