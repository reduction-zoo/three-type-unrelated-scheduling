import itertools,json
objectives=[(1,1,1),(2,3,5),(5,7,11),(6,10,15)]
directions=[{} for _ in objectives]
two_counts=[0]*len(objectives)
for p in itertools.product(range(1,13),repeat=3):
    exact=[[] for _ in range(61)]
    for x in range(60//p[0]+1):
        for y in range((60-p[0]*x)//p[1]+1):
            for z in range((60-p[0]*x-p[1]*y)//p[2]+1):
                exact[p[0]*x+p[1]*y+p[2]*z].append((x,y,z))
    for k,w in enumerate(objectives):
        best=-1;count=0;points=[]
        for T,configs in enumerate(exact):
            for x in configs:
                value=sum(a*b for a,b in zip(w,x))
                if value>best:best=value;count=1;points=[x]
                elif value==best:
                    count+=1
                    if len(points)<2:points.append(x)
            if T and count==2:
                u,v=sorted(points)
                delta=tuple(b-a for a,b in zip(u,v))
                assert sum(a*b for a,b in zip(w,delta))==0
                two_counts[k]+=1
                directions[k].setdefault(delta,{'processing':p,'capacity':T,'objective_value':best,'maximizers':[u,v]})
for w,n,ds in zip(objectives,two_counts,directions):
    print(json.dumps({'objective':w,'two_maximizer_knapsacks':n,'directions':[{'delta':d,**ds[d]} for d in sorted(ds)]}),flush=True)
