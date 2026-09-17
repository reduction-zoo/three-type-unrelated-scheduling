import argparse,itertools,json,subprocess,sys
from pathlib import Path
from fractions import Fraction
import z3

def execute(path,data,extract=False):
    command=[sys.executable,str(path)]+(['--extract'] if extract else [])
    return json.loads(subprocess.run(command,input=json.dumps(data),text=True,capture_output=True,check=True).stdout)

def check(path,a):
    source={'items':a}
    solutions=[list(s) for s in itertools.combinations(range(len(a)),len(a)//2) if 2*sum(a[i] for i in s)==sum(a)]
    target=execute(path,source)
    p,n,T=target['processing_times'],target['counts'],target['threshold']
    assert len(p)>0 and 1<=len(n)<=3 and type(T) is int and T>=0
    assert all(type(v) is int and v>=0 for v in n)
    assert all(len(row)==len(n) and all(type(v) is int and v>0 for v in row) for row in p)
    s=z3.Solver();x=[[z3.Int(f'job_{i}_{j}') for j in range(len(n))] for i in range(len(p))]
    for row in x:s.add(*[v>=0 for v in row])
    for j,count in enumerate(n):s.add(sum(row[j] for row in x)==count)
    for row,times in zip(x,p):s.add(sum(v*t for v,t in zip(row,times))<=T)
    if a and len(n)==3:
        k=max(a);w=(k,k+1,2*k+1)
        bounds=[]
        for row,times in zip(x,p):
            ratio=min(Fraction(t,c) for t,c in zip(times,w))
            bound=T*ratio.denominator//ratio.numerator
            bounds.append(bound)
            s.add(sum(c*v for c,v in zip(w,row))<=bound)
        if sum(c*v for c,v in zip(w,n))==sum(bounds):
            for row,bound in zip(x,bounds):s.add(sum(c*v for c,v in zip(w,row))==bound)
    calls=0;queries=0;recovered=[]
    while True:
        result=s.check();queries+=1
        if result==z3.unsat:break
        if result!=z3.sat:raise RuntimeError(str(result))
        model=s.model();schedule=[[model.eval(v).as_long() for v in row] for row in x]
        assert all(v>=0 for row in schedule for v in row)
        assert [sum(row[j] for row in schedule) for j in range(len(n))]==n
        assert all(sum(v*t for v,t in zip(row,times))<=T for row,times in zip(schedule,p))
        chosen=execute(path,{'source':source,'target_solution':schedule},True)
        assert isinstance(chosen,list) and all(type(i) is int for i in chosen)
        assert sorted(chosen) in solutions,{'source':source,'target':target,'schedule':schedule,'recovery':chosen}
        recovered.append(sorted(chosen));calls+=1
        s.add(z3.Or(*[v!=value for row,values in zip(x,schedule) for v,value in zip(row,values)]))
    assert bool(calls)==bool(solutions),{'source':source,'target':target,'expected':bool(solutions),'actual':bool(calls)}
    assert sorted(recovered)==sorted(solutions)
    return {'source':source,'target':target,'source_yes':bool(solutions),'solver_queries':queries,'target_witnesses':calls,'recovery_calls':calls,'recovered_subsets':recovered}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--candidate',required=True,type=Path);args=parser.parse_args()
    cases=[[]]
    for m,maximum in ((2,7),(4,7),(6,4)):
        cases.extend(map(list,itertools.combinations_with_replacement(range(1,maximum+1),m)))
    big=10**50
    cases.extend([[4,1,3,2],[3,1,3,3],[big,big+1,big+2,big+3],[big,big,big,big+2]])
    for a in cases:print(json.dumps(check(args.candidate,a)),flush=True)
