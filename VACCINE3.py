import math
try:
    t= int(input().strip())
except:
    pass
for i in range(t):
    x = [int(x) for x in input().split()]
    
    g=x[0]
    p=x[1]
   
    s=0
    n=11
    while n>g+1:
       
        s= s+x[n]
        n = n-1
    s1 = s + x[p+1]
   

    d1 = math.ceil((s+1)/p)
    d2 = math.ceil(s1/p)
    print(d1,d2)
    


        