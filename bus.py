for i in range(int(input())):
    n,m,q=map(int,input().split())
    z=0
    s=0
    l=[]
    for j in range(q):
        a,b=input().split()
        b=int(b)
        if a=='+':
            s=s+1
            l.append(b)
        else:
            s=s-1
            if b not in l:
                z=1
        if s>m :
            z=1
            
            
    if z==0:
        print("Consistent")
    else:
        print("Inconsistent")