from fractions import Fraction
from itertools import product
import json
checked=0
for p in product(range(1,5),repeat=3):
    for w in product(range(1,5),repeat=3):
        q=min(Fraction(t,c) for t,c in zip(p,w))
        for T in range(7):
            bound=T*q.denominator//q.numerator
            for x in product(range(T+1),repeat=3):
                if sum(t*v for t,v in zip(p,x))<=T:
                    assert sum(c*v for c,v in zip(w,x))<=bound
                    checked+=1
print(json.dumps({'valid_configuration_bound_checks':checked,'processing_vectors':64,'objective_vectors':64,'thresholds':7}))
