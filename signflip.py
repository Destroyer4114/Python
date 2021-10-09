for i in range(int(input())):
    n,k= map(int,input().split())
    a= list(map(int,input().split()))
    a.sort()
    s=0
    for j in range(n):
        if a[j]<0:
            if k>0:
                s+= -a[j]
                k -=1
        else:
            s= s+ a[j]
    print(s)
            