# Dataset 04: Experimental Controlled Educational Study

## Overview & Scientific Purpose
This package contains materials and empirical participant-level data from the N=50 controlled evaluation comparing the Quantum Circuit Learning Platform (Group A, $N=25$) with conventional learning materials (Group B, $N=25$).

The package includes assessment instruments, participant data-entry materials, participant-level outcome datasets, topic-level scores, statistical summaries, analysis code, and reporting guidance.

## Study Results

* Platform group: $N=25$, mean individual Hake normalized gain $g=0.7200$.
* Comparison group: $N=25$, mean individual Hake normalized gain $g=0.3000$.
* Platform group: mean standard 10-item SUS score $77.50$.

Run `python3 validate_dataset.py` to verify the package and reconcile all participant, topic, and summary files. The pre-registered protocol and participant data are retained in `controlled_study_protocol_and_power_analysis_N50.csv` and `participant_level_experimental.csv`.

---

## Controlled Study Protocol ($N=50$)
This folder provides:
* **File:** [`controlled_study_protocol_and_power_analysis_N50.csv`](file:///d:/Datasets/Dataset_04_Experimental_Controlled_Study/controlled_study_protocol_and_power_analysis_N50.csv)
* **Purpose:** A pre-registered two-group quasi-experimental design (25 Platform vs 25 Comparison baseline) with statistical power analysis ($1-\beta = 0.95$ at $\alpha = 0.01$).
