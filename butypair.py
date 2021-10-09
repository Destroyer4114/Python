def com(x):
    return x*(x-1)
for i in range(int(input())):
    n= int(input())
    l=[0]*(1000001)
    a=[int(x) for x in input().split()]
    for j in range(n):
        l[a[j]]  += 1
    ln=[com(x) for x in l]
    s= com(n)- sum(ln)
    print(s)
    


