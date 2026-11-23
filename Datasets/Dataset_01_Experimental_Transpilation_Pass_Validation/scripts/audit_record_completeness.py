#!/usr/bin/env python3
import argparse,csv
REQ=["circuit_id","pass_id","pass_name","compiler_name","compiler_version","backend_or_target","before_snapshot_file","after_snapshot_file","before_gate_count","after_gate_count","before_depth","after_depth","actual_transformation","generated_explanation_text","raw_trace_file","source_hash","record_provenance"]
p=argparse.ArgumentParser();p.add_argument("--input",required=True);p.add_argument("--out",required=True);a=p.parse_args()
with open(a.input,newline="",encoding="utf-8-sig") as f:rows=list(csv.DictReader(f))
out=[]
for r in rows:
 m=[k for k in REQ if not r.get(k,"").strip()]
 out.append({"record_id":r["record_id"],"missing_fields":";".join(m),"complete":not m,"status":"READY_FOR_REVIEW" if not m else "INCOMPLETE"})
with open(a.out,"w",newline="",encoding="utf-8-sig") as f:
 w=csv.DictWriter(f,fieldnames=["record_id","missing_fields","complete","status"]);w.writeheader();w.writerows(out)
print("records",len(rows),"complete",sum(x["complete"] for x in out))
