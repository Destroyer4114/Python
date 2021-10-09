for i in range(int(input())):
    n= int(input())
    a= [ int(x) for x in input().split()]
    t= [ int(x) for x in input().split()]
    res = {a[i]: t[i] for i in range(n)}
    r = {a[i]:i for i in range(n)}
    a.sort()
    s=0
    l=[]
    t1=0
    for j in range(n):
        if res[a[j]]>=a[j]+t1:
            # print("_",r[a[j]],t1,t1+a[j],j)
            l.append([r[a[j]]+1,t1,t1+a[j]])
            t1= t1+a[j]
            s= s+1
    print(s)
    print(r)
    for j in range(s):
        for k in range(3):
            print(l[j][k],end=' ')
        print("")
