#!/usr/bin/env python3
import argparse,csv,json
from collections import Counter
from sklearn.metrics import cohen_kappa_score,confusion_matrix
LABELS=["Correct","Partially correct","Incorrect"]
def read(p):
 with open(p,newline="",encoding="utf-8-sig") as f:return list(csv.DictReader(f))
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--e1",required=True);ap.add_argument("--e2",required=True);ap.add_argument("--adjudicated");ap.add_argument("--out",required=True);a=ap.parse_args()
 x={r["record_id"]:r["label"] for r in read(a.e1) if r.get("label") in LABELS}
 y={r["record_id"]:r["label"] for r in read(a.e2) if r.get("label") in LABELS}
 ids=sorted(set(x)&set(y))
 if not ids:raise SystemExit("No paired valid independent labels.")
 result={"paired_n":len(ids),"evaluator_1_counts":dict(Counter(x[i] for i in ids)),"evaluator_2_counts":dict(Counter(y[i] for i in ids)),"cohens_kappa":cohen_kappa_score([x[i] for i in ids],[y[i] for i in ids],labels=LABELS),"confusion_matrix_labels":LABELS,"confusion_matrix":confusion_matrix([x[i] for i in ids],[y[i] for i in ids],labels=LABELS).tolist()}
 if a.adjudicated:
  c=Counter(r["final_label"] for r in read(a.adjudicated) if r.get("final_label") in LABELS);n=sum(c.values())
  result.update({"adjudicated_n":n,"adjudicated_counts":dict(c),"strict_correct_pct":100*c["Correct"]/n if n else None,"partial_pct":100*c["Partially correct"]/n if n else None,"incorrect_pct":100*c["Incorrect"]/n if n else None})
 json.dump(result,open(a.out,"w"),indent=2);print(json.dumps(result,indent=2))
if __name__=="__main__":main()
