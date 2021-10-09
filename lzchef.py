t= int(input())
for i in range(t):
    s=0
    x,m,d=map(int,input().split())
    if x*m>x+d:
        s= x +d
    else:
        s= x*m
    print(s)