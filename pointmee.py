import collections
from typing import Counter
for i in range(int(input())):
    s=0
    n= int(input())
    x= list(map(int,input().split()))
    y= list(map(int,input().split()))
    xm= max(x)  
    ym= y[x.index(xm)]

    for i in range(n): 
        while x[i]<xm:
            s+=1
            if xm-x[i]>n:
                x[i]= x[i]+n 
                d=n
            else:
                d= xm-x[n]

                x[i]= xm
            
            if y[i]<ym:
                y[i]+=d
            elif y[i]>ym:
                y[i]-=d
  
        


                
            


