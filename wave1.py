n,q= map(int,input().split())
l= [int(x) for x in input().split()]
import numpy as np
p = np.poly1d(l)
for i in range(q):
    j= int(input())
    if p(j)>0:
        print("POSITIVE")
    elif  p(j)<0:
        print("POSITIVE")
    else:
        print("0")
