# Data Dictionary — Dataset 04: Experimental Controlled Educational Study

## Overview
This dictionary defines all variables and fields in the experimental controlled evaluation of the **Quantum Circuit Learning Platform** (Group A) compared against **Conventional Learning Materials** (Group B).

---

## 1. Participant and Study Design Variables
* **`participant_id`**: Anonymized participant identifier (`S001` to `S050`).
* **`study_group`**: 
  * `A_Platform`: Intervention group using the Quantum Circuit Learning Platform ($N=25$).
  * `B_Comparison`: Active control group using conventional learning materials ($N=25$).
* **`intervention`**: The specific learning condition assigned:
  * `Quantum Circuit Learning Platform`
  * `Conventional Learning Materials`
* **`consent_obtained`**: Participant informed consent recorded (`Yes` / `No`).
* **`ethics_approval_id`**: Institutional Review Board / Ethics Committee approval identifier (e.g., `ETH-2026-QC-04`).
* **`academic_program`**: Student degree programme (e.g., `Computer Science`, `Computer Engineering`, `Information Technology`).
* **`year_of_study`**: Year of undergraduate study (`1st year` to `4th year`).
* **`prior_quantum_experience`**: Baseline prior quantum computing background (`None`, `Basic`, `Intermediate`, `Advanced`).
* **`learning_time_minutes`**: Measured time-on-task during the instructional intervention (target: 45–75 minutes).

---

## 2. Knowledge Assessment Variables (20 Items)
Both pre-test and post-test contain 20 isomorphic binary-scored questions:
* **`pre_01` to `pre_20`**: Pre-test item scores ($1 = \text{Correct}$, $0 = \text{Incorrect}$).
* **`post_01` to `post_20`**: Post-test item scores ($1 = \text{Correct}$, $0 = \text{Incorrect}$).
* **`pre_correct`**: Total number of pre-test items answered correctly (integer, range: $0$ to $20$).
* **`post_correct`**: Total number of post-test items answered correctly (integer, range: $0$ to $20$).
* **`pre_percent`**: Pre-test score expressed as a percentage: $\frac{\text{pre\_correct}}{20} \times 100$.
* **`post_percent`**: Post-test score expressed as a percentage: $\frac{\text{post\_correct}}{20} \times 100$.
* **`gain_percentage_points`**: Absolute learning gain: $\text{post\_percent} - \text{pre\_percent}$.
* **`normalized_gain_g`**: Hake's normalized learning gain:
  $$g = \frac{S_{\text{post}} - S_{\text{pre}}}{100 - S_{\text{pre}}}$$
  *(For participants with $S_{\text{pre}} = 100$, $g$ is defined as $1.0$ if $S_{\text{post}} = 100$ and $0.0$ otherwise).*

---

## 3. Topic Mapping & Item Weights
The 20 items are partitioned into five core quantum computing topics:
1. **Circuit construction** (Items 1–5; 5 items = 25% test weight)
2. **Superposition and entanglement** (Items 6–10; 5 items = 25% weight)
3. **Transpilation and routing** (Items 11–14; 4 items = 20% weight)
4. **Hardware constraints** (Items 15–17; 3 items = 15% weight)
5. **Optimization** (Items 18–20; 3 items = 15% weight)

*Note: In `topic_scores_experimental.csv`, each participant has 5 rows containing item count, correct count, percentages, and normalized gains per topic.*

---

## 4. Platform Usability & Perceived Transparency Measures (Group A Only)
* **`sus_01` to `sus_10`**: Responses to the standard 10 System Usability Scale items (Brooke, 1996), scored on a 5-point Likert scale (1 = Strongly Disagree to 5 = Strongly Agree).
* **`sus_score`**: Standard composite SUS score ranging from $0$ to $100$:
  $$\text{SUS} = 2.5 \times \left[ \sum_{i \in \{1,3,5,7,9\}} (\text{sus}_i - 1) + \sum_{j \in \{2,4,6,8,10\}} (5 - \text{sus}_j) \right]$$
* **`transparency_rating_1_to_5`**: Student rating of platform internal process visibility and explanation clarity (1–5 scale).
* **`rating_circuit_builder_1_to_5`**: Rating of interactive visual circuit builder.
* **`rating_multi_framework_ide_1_to_5`**: Rating of multi-framework code editing environment.
* **`rating_transpilation_visualization_1_to_5`**: Rating of the 3D/graph transpilation visualizer.
* **`rating_ai_algorithm_tutor_1_to_5`**: Rating of the AI tutor guidance and step-by-step circuit explanation.

*(For Group B, usability and platform component ratings are recorded as blank/null).*
