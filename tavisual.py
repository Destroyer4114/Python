for i in range(int(input())):
    n,c,q=map(int,input().split())
    for j in range(q):
        l,r=map(int,input().split())
        c=l+r-c
    print(c)
