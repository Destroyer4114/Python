import math
for i in range(int(input())):
    n = int(input())
    a= [int(x) for x in input().split()]
    l=[0,a[0]]
    r=[a[n-1],0]
    for j in range(2,n):
        l.append(math.gcd(l[j-1],a[j-1]))
    for j in range(2,n):
        r.insert(0,math.gcd(r[0],a[n-j]))
    ans=[r[0]]
    for j in range(1,n-1):
        ans.append(math.gcd(l[j],r[j]))
    ans.append(l[n-1])
    b= max(ans)
    if ans.count(b)==1:
        a[ans.index(b)]=b
    else:
        a.sort()
        a[n-1]=b
    print(int(sum(a)/b))
        


