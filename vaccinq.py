for i in range(int(input())):
    n,p,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    t=0
    for j in range(p):
        if a[j]==0:
            t+=x
        else:
            t+=y
    print(t)