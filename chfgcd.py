import math
for i in range(int(input())):
    x,y=map(int,input().split())
    if x%2==0 and y%2==0:
        print(0)
    elif ((x%2==0 and y%2!=0) or (x%2!=0 and y%2==0)):
        if math.gcd(x,y)>1:
            print(0)
        else:
            print(1)
    else:
        if math.gcd(x,y)>1:
            print(0)
        elif math.gcd(x+1,y)>1:
            print(1)
        elif math.gcd(x,y+1)>1:
            print(1)
        else:
            print(2)
        

