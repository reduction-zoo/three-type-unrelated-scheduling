import argparse,json,math,sys
sys.set_int_max_str_digits(0)

def items(source):
    if not isinstance(source,dict) or set(source)!={'items'} or not isinstance(source['items'],list):
        raise ValueError('Expected an items list')
    a=source['items']
    if len(a)%2 or any(type(v) is not int or v<=0 for v in a):
        raise ValueError('Expected an even number of positive integers')
    return a

def forward(source):
    try:a=items(source)
    except ValueError:return {'invalid':True}
    if not a:return {'processing_times':[[1]],'counts':[0],'threshold':0}
    A=sum(a)
    if A%2:return {'processing_times':[[1]],'counts':[1],'threshold':0}
    m=len(a);k=max(a);H=4*(k+1)**2
    capacities=[H*(k+1)*(2*k+1-v)+v*(2*k+1-v) for v in a]
    T=math.prod(capacities)
    rows=[[(T//C)*p for p in (H*k+2*k+1-v,H*(k+1)+v,H*(2*k+1))] for v,C in zip(a,capacities)]
    return {'processing_times':rows,'counts':[A//2,m//2*(2*k+1)-A//2,m//2*(k+1)-A//2],'threshold':T}

def extract(source,schedule):
    a=items(source)
    if not a:
        if schedule!=[[0]]:raise ValueError('Invalid empty-instance witness')
        return []
    if not isinstance(schedule,list) or len(schedule)!=len(a):raise ValueError('Invalid number of machine rows')
    k=max(a);selected=[]
    for i,(v,row) in enumerate(zip(a,schedule)):
        if not isinstance(row,list) or len(row)!=3 or any(type(x) is not int for x in row):raise ValueError('Invalid count row')
        if row==[v,0,k+1-v]:selected.append(i)
        elif row!=[0,2*k+1-v,0]:raise ValueError('Invalid selector configuration')
    if len(selected)!=len(a)//2 or 2*sum(a[i] for i in selected)!=sum(a):raise ValueError('Invalid balanced selection')
    return selected

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--extract',action='store_true');args=parser.parse_args()
    try:data=json.load(sys.stdin)
    except json.JSONDecodeError:
        if args.extract:raise
        print(json.dumps({'invalid':True}));sys.exit(0)
    if args.extract:result=extract(data['source'],data['target_solution'])
    else:result=forward(data)
    print(json.dumps(result))
