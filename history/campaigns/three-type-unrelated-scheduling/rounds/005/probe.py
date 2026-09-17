import itertools,json,math,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
from check import solve
published={'processing_times':[[6,10,15]]*2,'counts':[4,2,1],'threshold':30}
assert solve(published) is None
print(json.dumps({'published_instance':published,'target_yes':False}))
for p,q,r in itertools.combinations(range(2,12),3):
    if any(math.gcd(a,b)!=1 for a,b in itertools.combinations((p,q,r),2)):continue
    T=p*q*r
    full=[(x,y,z) for x in range(p+1) for y in range(q+1) for z in range(r+1) if q*r*x+p*r*y+p*q*z==T]
    assert full==[(0,0,r),(0,q,0),(p,0,0)]
    print(json.dumps({'denominators':[p,q,r],'full_configurations':full}))
