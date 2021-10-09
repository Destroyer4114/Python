t= int(input())
for i in range(t):
    n= int(input())
    a= list(map(int,input().split()))
    b=list(set(a))
    c=b
    s=1
    if 0 in b:
        b.remove(0)
    if 1 in b:
        b.remove(1)
    if (-1) in  b:
        b.remove(-1)
        if len(b)!=0:
            s=0
        if a.count(-1)>1:
            if a.count(1)==0:
                s=0
    else:
        if len(b)>1:
            s=0
        elif len(b)==1:
            if a.count(b[0])!=1: 
                s=0
    print(s)

    

