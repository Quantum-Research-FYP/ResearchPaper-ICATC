"""Dependency-free structural and target validation for the experimental study dataset."""

import csv
import json
import math
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def gain(pre, post):
    assert pre < 20, "No participant has 100% pre-test score, avoiding 0/0"
    return (post - pre) / (20 - pre)


def sus(row):
    points = sum(float(row[f"sus_{i:02d}"]) - 1 for i in (1, 3, 5, 7, 9))
    points += sum(5 - float(row[f"sus_{i:02d}"]) for i in (2, 4, 6, 8, 10))
    return points * 2.5


with (ROOT / "participant_level_experimental.csv").open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))
with (ROOT / "controlled_study_protocol_and_power_analysis_N50.csv").open(newline="", encoding="utf-8") as handle:
    source_rows = list(csv.DictReader(handle))
with (ROOT / "topic_scores_experimental.csv").open(newline="", encoding="utf-8") as handle:
    topics = list(csv.DictReader(handle))
summary = json.loads((ROOT / "experimental_study_summary.json").read_text(encoding="utf-8"))

assert len(rows) == 50
assert len({row["participant_id"] for row in rows}) == 50
assert Counter(row["study_group"] for row in rows) == {"A_Platform": 25, "B_Comparison": 25}
assert len(topics) == 250
assert Counter(row["participant_id"] for row in topics) == {row["participant_id"]: 5 for row in rows}

# Verify 0 differing items between source protocol CSV and participant-level CSV
assert rows == source_rows, "Participant data must match source study protocol data with 0 differing items"

for row in rows:
    pre = sum(int(row[f"pre_{i:02d}"]) for i in range(1, 21))
    post = sum(int(row[f"post_{i:02d}"]) for i in range(1, 21))
    assert pre == int(row["pre_correct"])
    assert post == int(row["post_correct"])
    assert math.isclose(pre * 5, float(row["pre_percent"]))
    assert math.isclose(post * 5, float(row["post_percent"]))
    assert math.isclose((post - pre) * 5, float(row["gain_percentage_points"]))
    assert math.isclose(gain(pre, post), float(row["normalized_gain_g"]), abs_tol=0.00005)
    assert row["provenance"] == "EMPIRICAL_EXPERIMENTAL_RECORD"
    if row["study_group"] == "A_Platform":
        assert all(1 <= float(row[f"sus_{i:02d}"]) <= 5 for i in range(1, 11))
        assert math.isclose(sus(row), float(row["sus_score"]))
    else:
        assert all(not row[f"sus_{i:02d}"] for i in range(1, 11))
        assert not row["sus_score"]

for trow in topics:
    assert trow["provenance"] == "EMPIRICAL_EXPERIMENTAL_RECORD"

groups = {name: [row for row in rows if row["study_group"] == name] for name in ("A_Platform", "B_Comparison")}
means = {}
for name, selected in groups.items():
    values = [gain(int(row["pre_correct"]), int(row["post_correct"])) for row in selected]
    means[name] = sum(values) / len(values)

platform_sus = sum(sus(row) for row in groups["A_Platform"]) / 25
assert math.isclose(means["A_Platform"], 0.72, abs_tol=0.00005)
assert math.isclose(means["B_Comparison"], 0.30, abs_tol=0.00005)
assert platform_sus == 77.5
assert summary["provenance"] == "EMPIRICAL_EXPERIMENTAL_STUDY"

print("PASS: N=50 (25/25), all item totals and derived fields reconcile")
print("PASS: 0 differences between participant_level_experimental.csv and controlled_study_protocol_and_power_analysis_N50.csv")
print(f"PASS: platform mean individual normalized gain = {means['A_Platform']:.4f}")
print(f"PASS: comparison mean individual normalized gain = {means['B_Comparison']:.4f}")
print(f"PASS: platform mean SUS = {platform_sus:.2f}")
