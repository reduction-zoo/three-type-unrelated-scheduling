import argparse,itertools,json,subprocess,sys,tempfile
from pathlib import Path
import z3

def source_data(s):
    assert set(s)=={'items'} and isinstance(s['items'],list)
    a=s['items'];assert len(a)%2==0 and all(type(v) is int and v>0 for v in a)
    return a

def source_witness(s,w):
    a=source_data(s)
    return isinstance(w,list) and all(type(i) is int and 0<=i<len(a) for i in w) and len(set(w))==len(w)==len(a)//2 and 2*sum(a[i] for i in w)==sum(a)

def source(s):
    a=source_data(s)
    return next((list(w) for w in itertools.combinations(range(len(a)),len(a)//2) if 2*sum(a[i] for i in w)==sum(a)),None)

def target_data(t):
    assert set(t)=={'processing_times','counts','threshold'}
    p,n,T=t['processing_times'],t['counts'],t['threshold']
    assert isinstance(n,list) and 1<=len(n)<=3 and all(type(v) is int and v>=0 for v in n)
    assert isinstance(p,list) and p and all(isinstance(row,list) and len(row)==len(n) and all(type(v) is int and v>0 for v in row) for row in p)
    assert type(T) is int and T>=0
    return p,n,T

def witness(t,w):
    p,n,T=target_data(t)
    return isinstance(w,list) and len(w)==len(p) and all(isinstance(row,list) and len(row)==len(n) and all(type(v) is int and v>=0 for v in row) for row in w) and all(sum(row[j] for row in w)==n[j] for j in range(len(n))) and all(sum(a*b for a,b in zip(pi,xi))<=T for pi,xi in zip(p,w))

def encoding(t):
    p,n,T=target_data(t);x=[[z3.Int(f'x_{i}_{j}') for j in range(len(n))] for i in range(len(p))];s=z3.Solver()
    s.add(*[v>=0 for row in x for v in row],*[z3.Sum([row[j] for row in x])==n[j] for j in range(len(n))],*[z3.Sum([a*b for a,b in zip(pi,xi)])<=T for pi,xi in zip(p,x)])
    return s,x

def answer(t,s,x):
    r=s.check()
    if r==z3.unsat:return None
    if r!=z3.sat:raise RuntimeError(str(r))
    m=s.model();w=[[m.eval(v).as_long() for v in row] for row in x];assert witness(t,w);return w

def solve(t):
    s,x=encoding(t);return answer(t,s,x)

def run_candidate(path,case):
    src=case['source'];r=subprocess.run([sys.executable,str(path)],input=json.dumps(src),text=True,capture_output=True,check=True);target=json.loads(r.stdout);target_data(target);s,x=encoding(target);calls=0
    for _ in range(3):
        w=answer(target,s,x)
        if calls==0:assert (w is not None)==case['yes'],{'source':src,'target':target,'witness':w}
        if w is None:break
        r=subprocess.run([sys.executable,str(path),'--extract'],input=json.dumps({'source':src,'target_solution':w}),text=True,capture_output=True,check=True);recovered=json.loads(r.stdout);assert source_witness(src,recovered);calls+=1
        s.add(z3.Or(*[v!=a for row,wr in zip(x,w) for v,a in zip(row,wr)]))
    return calls

def self_test(cases):
    for case in cases:
        w=source(case['source']);assert (w is not None)==case['yes']
        if w is not None:assert source_witness(case['source'],w)
    checked=0;negative=0
    for values in itertools.product((1,2),repeat=6):
        for T in (1,2,3):
            t={'processing_times':[list(values[:3]),list(values[3:])],'counts':[1,1,1],'threshold':T}
            expected=any(witness(t,[list(row),[1-v for v in row]]) for row in itertools.product((0,1),repeat=3));w=solve(t);assert (w is not None)==expected;checked+=1;negative+=not expected
    t={'processing_times':[[1]],'counts':[0],'threshold':0};assert solve(t)==[[0]]
    assert not witness(t,[[True]]) and not witness(t,[[-1]])
    assert not source_witness({'items':[1,1,1,1]},[0,0])
    fixtures={
      'malformed':"import json;print(json.dumps({'invalid':True}))",
      'wrong_decision':"import json;print(json.dumps({'processing_times':[[1]],'counts':[0],'threshold':0}))",
      'wrong_recovery':"import json,sys;print(json.dumps([] if '--extract' in sys.argv else {'processing_times':[[1]],'counts':[0],'threshold':0}))"}
    for label,code in fixtures.items():
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/'fault.py';p.write_text(code)
            try:run_candidate(p,{'source':{'items':[1,2] if label=='wrong_decision' else [1,1]},'yes':label!='wrong_decision'})
            except AssertionError:pass
            else:raise AssertionError(label)
    print(json.dumps({'solver':z3.get_version_string(),'source_cases':len(cases),'target_crosschecks':checked,'target_unsat':negative,'zero_job_check':1,'rejected_subprocess_fixtures':list(fixtures)}))

if __name__=='__main__':
    parser=argparse.ArgumentParser();group=parser.add_mutually_exclusive_group(required=True);group.add_argument('--self-test',action='store_true');group.add_argument('--candidate',type=Path);args=parser.parse_args();cases=json.loads((Path(__file__).parent/'cases.json').read_text())
    if args.self_test:self_test(cases)
    else:
        for case in cases:print(json.dumps({'source':case['source'],'yes':case['yes'],'recovery_calls':run_candidate(args.candidate,case)}),flush=True)
