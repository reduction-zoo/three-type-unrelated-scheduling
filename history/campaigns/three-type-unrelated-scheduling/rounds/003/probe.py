import sys,json,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from check import witness
rows=[json.loads(l) for l in (Path(__file__).resolve().parents[4]/'research/evidence/three-type-unrelated-scheduling/output.jsonl').read_text().splitlines()]
for row in rows:
    a=row['source'];A=sum(a);m=len(a);T=(A+1)**4*math.prod(a)
    target={'processing_times':[[T//v-v-1,T//v,v] for v in a],'counts':[A//2,A//2,A//2+m//2],'threshold':T}
    selected=set(sorted(range(m),key=lambda i:(a[i],i))[:m//2]);x=[v if i in selected else 0 for i,v in enumerate(a)];left=A//2-sum(x)
    assert left>=0
    for i,v in enumerate(a):
        if i in selected:continue
        added=min(left,v);x[i]=added;left-=added
    w=[[x[i],v-x[i],x[i]+int(i in selected)] for i,v in enumerate(a)]
    assert left==0 and witness(target,w)
    print(json.dumps({'source':a,'source_yes':row['source_solution'] is not None,'target':target,'witness':w,'target_yes':True}),flush=True)
