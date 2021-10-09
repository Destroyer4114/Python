import math

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



def cD(n) :
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) :
        if (n % i == 0) :
            if (n / i == i) :
                cnt = cnt + 1
            else : # Otherwise count both   
                cnt = cnt + 2
                 
    return cnt
# print(cD(int(input())))

for a in range(int(input())):
    n,e= map(int,input().split())
    s=0
    s1=0

    m=1000000007
    for b in range(1,n+1):
        s= (s%m+(mp(b,e,m)*(cD(b)%m))%m)%m
        s1+=pow(b,e,m)
        print(s)
    print(s)    