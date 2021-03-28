r,o,c  = [int(x) for x in input().split()]
i= 20-o
m= i*36
while 0<=c<=r<= 720 and 1<= o<= 19 and 0<= c <= 36*o:
    if m > (r-c):
        print("YES")
    else:
        print("NO")
    break
        
