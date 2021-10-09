import math
for i in range(int(input())):
    a,b= map(int,input().split())
    x=int((a+b)*(0.5))
    if a==b:
        k= 0
    else:
        k= max(math.ceil((b-x)/2)+math.ceil((x-a)/2),math.ceil((b-x-1)/2)+math.ceil((x-a+1)/2))
    print(int(k))   