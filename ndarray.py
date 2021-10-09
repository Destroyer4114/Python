import math
for i in range(int(input())):
    n= int(input())
    a= list(map(int,input().split()))
    b=[a[0]]
    print(a[0],end=' ')
    for j in range(1,n):
        r=a[j] 
        if b[j-1]>r:
            l= math.ceil((b[j-1]-r)/r)
            r+= a[j]*l
        
        
        b.append(r)
        print(b[j],end=' ')
    print()
