import collections
from typing import Counter
for i  in range(int(input())):
    n,k= map(int,input().split())
    s=list(map(int,input().split()))
    c= Counter(s)
    l= list(set(s))
    l.sort(reverse= True)
    r=0
    i=0
    while r>=k:
        r+=c[l[i]]
        i+=1
    print(r)

   

    