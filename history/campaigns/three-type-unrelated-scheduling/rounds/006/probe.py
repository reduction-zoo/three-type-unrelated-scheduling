import itertools,json,math
for lengths in itertools.combinations(range(2,13),3):
    if math.gcd(*lengths)!=1:continue
    a,b,c=lengths
    fibers=[[] for _ in range(241)]
    for x in range(241//a+1):
        for y in range((240-a*x)//b+1):
            for z in range((240-a*x-b*y)//c+1):
                fibers[a*x+b*y+c*z].append((x,y,z))
    pairs=[(C,sorted(v)) for C,v in enumerate(fibers) if len(v)==2]
    differences=sorted({tuple(v[1][j]-v[0][j] for j in range(3)) for C,v in pairs})
    assert len(differences)<=3
    print(json.dumps({'lengths':lengths,'two_point_fibers':pairs,'differences':differences}))
