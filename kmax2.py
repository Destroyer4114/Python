for i in range(int(input())):
    n,k=map(int,input().split())
    a= list(map(int,input().split()))
    b=max(a)
    c=[]
    lc=0
    for j in range(n):
        if a[j]==b:
            c.append(j)
            lc+=1
    s=0
    for j in range(lc):
        if c[j]>=(k-1):
            s=s+(n-c[j])
    print(s)


    
    

