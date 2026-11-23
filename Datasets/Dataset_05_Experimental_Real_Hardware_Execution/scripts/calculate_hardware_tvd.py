#!/usr/bin/env python3
"""Calculate per-execution TVD from actual hardware counts and ideal probabilities."""
import argparse,csv,math
from collections import defaultdict
def read(p):
    with open(p,newline="",encoding="utf-8-sig") as f:return list(csv.DictReader(f))
def main():
    a=argparse.ArgumentParser()
    a.add_argument("--counts",required=True);a.add_argument("--ideal",required=True);a.add_argument("--out",required=True)
    x=a.parse_args(); counts=read(x.counts); ideal=read(x.ideal)
    runs=defaultdict(lambda:defaultdict(int)); refs=defaultdict(dict)
    for r in counts:
        k=(r["experiment_id"],r["execution_id"],r["circuit_id"],r["hardware_id"])
        runs[k][r["bitstring_canonical"]]+=int(r["count"])
    for r in ideal:refs[r["circuit_id"]][r["logical_bitstring_canonical"]]=float(r["ideal_probability"])
    out=[]
    for k,cts in runs.items():
        exp,eid,cid,hw=k; n=sum(cts.values())
        if not n:raise ValueError(f"Empty counts: {k}")
        q=refs.get(cid)
        if not q:raise ValueError(f"Missing ideal reference: {cid}")
        if not math.isclose(sum(q.values()),1,abs_tol=1e-6):raise ValueError(f"Ideal probabilities for {cid} do not sum to 1")
        p={b:v/n for b,v in cts.items()}
        dist=.5*sum(abs(p.get(b,0)-q.get(b,0)) for b in set(p)|set(q))
        for b in sorted(set(p)|set(q)):
            out.append(dict(experiment_id=exp,execution_id=eid,circuit_id=cid,hardware_id=hw,
              bitstring_canonical=b,count=cts.get(b,0),shots_returned=n,
              observed_probability=p.get(b,0),ideal_probability=q.get(b,0),
              absolute_difference=abs(p.get(b,0)-q.get(b,0)),tvd_for_execution=dist))
    with open(x.out,"w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
    print("Wrote",len(out),"rows to",x.out)
if __name__=="__main__":main()
