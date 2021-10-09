import math
t= int(input())
for i in range(t):
    a,b,x,y= map(int,input().split())
    print(math.ceil(x/a)+math.ceil(y/b))
