

def mp(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y 

n,k=map(int,input().split())
m=10000007
while n!=0:
    a=mp(n,n,m)
    
    b=int(mp(n,k,m))
    c=int((2*mp(n-1,k,m))%m)
    d=int((2*mp(n-1,n-1,m))%m)
    s= (int((a+b)%m) + int((c+d)%m))%m
    print(s)
    n,k=map(int,input().split())
    