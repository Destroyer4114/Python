t=int(input())
for i in range(t):
    n,m,x=map(int,input().split())
    l=list(map(int,input().split()))
    s=[i+1 for i in range(len(l)) if l[i]>=m]
    uss= [i for i in l if i<m]
    while(len(s)<x):
        p=l.index(max(uss))
        q=uss.index(max(uss))
        s.append(p+1)
        uss.pop(q)
    s.sort()
    print(len(s),end=" ")
    for i in s:
        print(i,end=" ")
    print()
        