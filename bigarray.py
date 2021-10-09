for i in range(int(input())):
    n,s= map(int,input().split())
    r =n*(n+1)//2
    v= r-s
    if v>=1 and v<=n:
        print(v)
    else:
        print(-1)