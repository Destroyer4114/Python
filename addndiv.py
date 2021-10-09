import math
for i in range(int(input())):
    a,b=map(int,input().split())
    if a==1:
        print("YES")
    else:
        r=0
        while math.gcd(a,b)!=1:
            a=a//math.gcd(a,b)
            if a==1:
                r=1
                break
            
            
        if r==0:
            print("NO")
        else:
            print("YES")