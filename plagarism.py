for i in range(int(input())):
    n,m,k= map(int,input().split())
    l=list(map(int,input().split()))
    c=[0]*(n+m+1)
    
    for j in range(k):
        c[l[j]]+=1
    d= []
    for j in range(1,n+1):
        if c[j]>1:
            d.append(j)
    print(len(d),end=' ')
    for j in range(len(d)):
        print(d[j],end=' ')
    print()



    