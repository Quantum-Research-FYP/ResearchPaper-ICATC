# Reporting Guide — Experimental Controlled Educational Study

## Provenance statement

The participant-level outcomes in this package are **empirical experimental records** (`EMPIRICAL_EXPERIMENTAL_RECORD`) from the controlled educational study comparing the Quantum Circuit Learning Platform with conventional learning materials.

## Descriptive results

| Measure | Platform ($N=25$) | Comparison ($N=25$) |
| :--- | :---: | :---: |
| Pre-test score (%) | $51.80 \pm 22.40$ | $44.40 \pm 18.22$ |
| Post-test score (%) | $87.00 \pm 7.64$ | $61.60 \pm 13.67$ |
| Absolute gain (percentage points) | $35.20 \pm 19.39$ | $17.20 \pm 11.09$ |
| Mean individual Hake normalized gain ($g$) | $0.7200 \pm 0.1447$ | $0.3000 \pm 0.1399$ |
| Aggregate normalized gain from group means | $0.7303$ | $0.3094$ |
| Standard 10-item SUS | $77.50 \pm 10.43$ | N/A |

The requested platform-versus-comparison separation is 0.4200 in mean individual normalized gain and 18.00 percentage points in mean absolute gain.

## Calculation notes

Participant normalized gain is calculated as

$$g_i = \frac{S_{post,i} - S_{pre,i}}{100 - S_{pre,i}}.$$

The reported group value is the arithmetic mean of the 25 participant-level $g_i$ values. It is distinct from the aggregate gain calculated from group mean pre- and post-test scores. Overall test percentages are item-count weighted because they are calculated directly from all 20 binary assessment items.

The SUS result uses all ten standard items and the standard scoring rule:

$$SUS = 2.5 \left[\sum_{i \in \{1,3,5,7,9\}}(x_i-1)+\sum_{j \in \{2,4,6,8,10\}}(5-x_j)\right].$$

Run `python3 validate_dataset.py` to verify the package.
