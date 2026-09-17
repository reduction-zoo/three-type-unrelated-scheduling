import json
for k in range(1,9):
    w=(k,k+1,2*k+1);H=4*(k+1)**2
    for a in range(1,k+1):
        b=(k+1)*(2*k+1-a);s=a*(2*k+1-a)
        p=(H*k+2*k+1-a,H*(k+1)+a,H*(2*k+1));C=H*b+s
        best=-1;maximizers=[];count=0
        for x in range(C//p[0]+1):
            for y in range((C-p[0]*x)//p[1]+1):
                for z in range((C-p[0]*x-p[1]*y)//p[2]+1):
                    count+=1;value=k*x+(k+1)*y+(2*k+1)*z
                    if value>best:best=value;maximizers=[(x,y,z)]
                    elif value==best:maximizers.append((x,y,z))
        assert best==b and sorted(maximizers)==[(0,2*k+1-a,0),(a,0,k+1-a)]
        print(json.dumps({'k':k,'a':a,'processing':p,'capacity':C,'maximum':best,'maximizers':maximizers,'configurations_checked':count}),flush=True)
