t=int(input())
for i in range(t):  
    n,k,f= map(int,input().split())
    s=0
    x=0
    for j in range(n):
        a,b=map(int,input().split())
        if a>x:
            s= s+ (a-x)

        
        x=b
    s= s+ (f-x)
    if s>=k:
        print("YES")
    else:
        print("NO")


