n,q= map(int,input().split())
s=1
l= [int(x) for x in input().split()]
x=
for i in range(n):
    s = s*(x-l[i])
for i in range(q):
    s=0
    a= int(input())
    while a<l[s] and s<n-1:
        s= s+1
    if a<l[n-1]:
        if (n-1)%2==0:
            print("NEGATIVE")
        else:
            print("POSITIVE")

    elif a==l[s]:
        print("0")
    elif s%2==0:
        print("POSITIVE")
    else:
        print("NEGATIVE")
