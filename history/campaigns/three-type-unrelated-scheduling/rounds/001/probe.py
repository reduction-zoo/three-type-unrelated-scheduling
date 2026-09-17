import sys,json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from check import witness
rows=[json.loads(l) for l in (Path(__file__).resolve().parents[4]/'research/evidence/three-type-unrelated-scheduling/output.jsonl').read_text().splitlines()]
for row in rows:
    a=row['source'];A=sum(a);m=len(a);H=A**3
    target={'processing_times':[[H+A-v,H-v,A*H] for v in a],'counts':[A//2,(m-1)*A//2,m//2],'threshold':A*H}
    chosen=sorted(range(m),key=lambda i:(-a[i],i))[:m//2];w=[[0,0,1] for _ in a];left=A//2
    for i in chosen:
        used=min(a[i],left);w[i]=[used,A-used,0];left-=used
    assert left==0 and witness(target,w)
    print(json.dumps({'source':a,'source_yes':row['source_solution'] is not None,'target':target,'witness':w,'target_yes':True}),flush=True)
