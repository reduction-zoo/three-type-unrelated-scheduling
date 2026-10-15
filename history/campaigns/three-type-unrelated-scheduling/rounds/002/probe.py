import sys,json,random
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from check import encoding,answer,witness

def intervals(p,b,T,z):
    slope=p[0]-p[1];rhs=T-p[1]*b-p[2]*z
    if slope>0:return 0,min(b,rhs//slope)
    if slope<0:return max(0,-((-rhs)//slope)),b
    return (0,b) if rhs>=0 else (1,0)

def construct(t,b):
    p,n,T=t['processing_times'],t['counts'],t['threshold'];X,_,K=n
    if K>len(p):return None
    initial=[intervals(row,total,T,0) for row,total in zip(p,b)]
    if any(lo>hi for lo,hi in initial):return None
    left=[];right=[];selected_intervals={}
    for i,(row,total,(lo,hi)) in enumerate(zip(p,b,initial)):
        lower,upper=intervals(row,total,T,1)
        if lower>upper:continue
        assert lower>=lo and upper<=hi and (lower==lo or upper==hi)
        selected_intervals[i]=(lower,upper)
        if lower>lo:left.append((lower-lo,i))
        else:right.append((hi-upper,i))
    left.sort();right.sort()
    for count in range(K+1):
        other=K-count
        if count>len(left) or other>len(right):continue
        chosen={i for _,i in left[:count]+right[:other]}
        bounds=[selected_intervals[i] if i in chosen else initial[i] for i in range(len(p))]
        if sum(lo for lo,hi in bounds)<=X<=sum(hi for lo,hi in bounds):
            values=[lo for lo,hi in bounds];remaining=X-sum(values)
            for i,(lo,hi) in enumerate(bounds):
                add=min(remaining,hi-lo);values[i]+=add;remaining-=add
            assert remaining==0
            return [[v,total-v,int(i in chosen)] for i,(v,total) in enumerate(zip(values,b))]
    return None

if __name__=='__main__':
    rng=random.Random(20260916)
    for sample in range(192):
        m=rng.randint(2,6);b=[rng.randint(1,4) for _ in range(m)];X=rng.randint(0,sum(b));K=rng.randint(0,m)
        t={'processing_times':[[rng.randint(1,9) for _ in range(3)] for _ in range(m)],'counts':[X,sum(b)-X,K],'threshold':rng.randint(0,40)}
        s,x=encoding(t);s.add(*[row[0]+row[1]==total for row,total in zip(x,b)],*[row[2]<=1 for row in x]);expected=answer(t,s,x);w=construct(t,b)
        assert (w is not None)==(expected is not None),(t,b,w,expected)
        if w is not None:assert witness(t,w) and all(row[0]+row[1]==total and row[2]<=1 for row,total in zip(w,b))
        print(json.dumps({'sample':sample,'target':t,'fixed_totals':b,'sat':expected is not None,'solver_witness':expected,'constructed_witness':w}),flush=True)
