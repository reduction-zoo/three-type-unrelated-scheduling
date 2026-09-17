"""Independent bounded review checks; no candidate or checker imports."""
import itertools
import json
import subprocess
import sys
from pathlib import Path

sys.set_int_max_str_digits(0)
campaign = Path(__file__).resolve().parents[2]
candidate = campaign / 'work/algorithm.py'

def invoke(data, extract=False):
    result = subprocess.run([sys.executable, str(candidate)] + (['--extract'] if extract else []),
                            input=json.dumps(data), text=True, capture_output=True, check=True)
    return json.loads(result.stdout)

pairs = configurations = 0
for k in range(1, 21):
    for a in range(1, k + 1):
        h = 4 * (k + 1)**2
        p = (h*k + 2*k+1-a, h*(k+1)+a, h*(2*k+1))
        b = (k+1)*(2*k+1-a)
        capacity = h*b + a*(2*k+1-a)
        maximizers = set()
        for x in range(capacity//p[0] + 1):
            for z in range((capacity-p[0]*x)//p[2] + 1):
                for y in range((capacity-p[0]*x-p[2]*z)//p[1] + 1):
                    configurations += 1
                    objective = k*x + (k+1)*y + (2*k+1)*z
                    assert objective <= b
                    if objective == b:
                        maximizers.add((x,y,z))
        assert maximizers == {(0,2*k+1-a,0), (a,0,k+1-a)}
        pairs += 1
print(json.dumps({'local_pairs':pairs, 'feasible_configurations':configurations}))

for a in ([], [1,2], [1,2,2,3], [1,1,1,3], [3,2,1,4]):
    source = {'items':a}
    target = invoke(source)
    rows, counts, capacity = target['processing_times'], target['counts'], target['threshold']
    choices = [[v for v in itertools.product(*(range(n+1) for n in counts))
                if sum(p*x for p,x in zip(row,v)) <= capacity] for row in rows]
    recovered = []
    for schedule in itertools.product(*choices):
        if any(sum(row[j] for row in schedule) != n for j,n in enumerate(counts)):
            continue
        chosen = invoke({'source':source,'target_solution':schedule}, True)
        assert len(chosen) == len(set(chosen)) == len(a)//2
        assert all(type(i) is int and 0 <= i < len(a) for i in chosen)
        assert 2*sum(a[i] for i in chosen) == sum(a)
        recovered.append(tuple(sorted(chosen)))
    expected = [s for s in itertools.combinations(range(len(a)),len(a)//2)
                if 2*sum(a[i] for i in s) == sum(a)]
    assert sorted(recovered) == sorted(expected)
    print(json.dumps({'source':a,'independently_enumerated_target_witnesses':len(recovered)}))

# Exercise actual serialization beyond Python's default 4300-digit ceiling.
large = 10**5000
source = {'items':[large,large]}
target = invoke(source)
for schedule in ([[large,0,1],[0,large+1,0]], [[0,large+1,0],[large,0,1]]):
    assert [sum(row[j] for row in schedule) for j in range(3)] == target['counts']
    assert all(sum(p*x for p,x in zip(row,v)) == target['threshold']
               for row,v in zip(target['processing_times'],schedule))
    chosen = invoke({'source':source,'target_solution':schedule},True)
    assert len(chosen)==1 and chosen[0] in (0,1)
print(json.dumps({'decimal_digits_per_source_item':5001,'large_witnesses':2,
                  'threshold_bits':target['threshold'].bit_length()}))

records = [json.loads(line) for line in (campaign/'rounds/009/verification-output.jsonl').read_text().splitlines()]
assert len(records)==327
assert sum(r['source_yes'] for r in records)==94
assert sum(r['target_witnesses'] for r in records)==521
assert sum(r['solver_queries'] for r in records)==848
print(json.dumps({'raw_log_counts_reconciled':True}))
