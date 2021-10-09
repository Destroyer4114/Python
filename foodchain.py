for i in range(int(input())):
    e,k=map(int,input().split())
    n=0
    while e>0:
        n= n+1
        e= int(e/k)
    print(n-1)

