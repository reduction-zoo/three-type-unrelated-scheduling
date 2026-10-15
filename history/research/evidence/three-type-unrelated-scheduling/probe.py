import itertools,json,z3

def source(a):
    return next((list(s) for s in itertools.combinations(range(len(a)),len(a)//2) if 2*sum(a[i] for i in s)==sum(a)),None)

def solve(p,n,T):
    x=[[z3.Int(f'x_{i}_{j}') for j in range(len(n))] for i in range(len(p))];s=z3.Solver()
    s.add(*[v>=0 for row in x for v in row])
    s.add(*[z3.Sum([row[j] for row in x])==n[j] for j in range(len(n))])
    s.add(*[z3.Sum([a*b for a,b in zip(pi,xi)])<=T for pi,xi in zip(p,x)])
    status=s.check()
    if status==z3.unsat:return None
    if status!=z3.sat:raise RuntimeError(str(status))
    model=s.model();w=[[model.eval(v).as_long() for v in row] for row in x]
    assert all(v>=0 for row in w for v in row)
    assert all(sum(row[j] for row in w)==n[j] for j in range(len(n)))
    assert all(sum(a*b for a,b in zip(pi,xi))<=T for pi,xi in zip(p,w))
    return w

cases=[];counts={True:0,False:0}
for m in (4,6):
    for a in itertools.combinations_with_replacement(range(1,6),m):
        A=sum(a)
        if A%2 or any(2*(A**4-v*(A**3+A-v))<=A**4 for v in a):continue
        answer=source(a);yes=answer is not None
        if counts[yes]>=12:continue
        counts[yes]+=1;cases.append((a,answer))
assert counts=={True:12,False:12}
for a,answer in cases:
    A=sum(a);m=len(a);T=A**4
    baseline=[[A**3+A-v,A**3-v,A**2,T-v*A**2] for v in a]
    n=[A//2,(m-1)*A//2,A//2,m//2]
    w=solve(baseline,n,T);assert (w is not None)==(answer is not None)
    candidate=[[A**3+A-v,A**3-v,T-v*(A**3+A-v)] for v in a]
    multiplicities=[A,(m-1)*A//2,m//2];cw=solve(candidate,multiplicities,T)
    print(json.dumps({'source':a,'source_solution':answer,'baseline_sat':w is not None,'baseline_witness':w,'candidate':{'processing_times':candidate,'counts':multiplicities,'threshold':T},'candidate_sat':cw is not None,'candidate_witness':cw}),flush=True)
