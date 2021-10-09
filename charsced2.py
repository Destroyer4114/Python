for i in range(int(input())):
    n= int(input())
    a= [ int(x) for x in input().split()]
    t= [ int(x) for x in input().split()]
    res=[[] for _ in range(3*100000+1)]
    r=[[] for _ in range(3*100000+1)]
    ct=[0]*(3*100000+1)
    # [[5,3,4,6,2],[4,5], [5,6],7]
    # res = {a[i]:t[i] for i in range(n)}
    # r = {a[i]:i for i in range(n)}
    for j in range(n):
        res[a[j]].append(t[j])
        r[a[j]].append(j)
    a.sort()
    s=0
    l=[]
    t1=0
    for j in range(n):
        if res[a[j]][ct[a[j]]]>=a[j]+t1:

            # print("_",r[a[j]],t1,t1+a[j],j)
            l.append([r[a[j]][ct[a[j]]]+1,t1,t1+a[j]])
            t1= t1+a[j]
            s= s+1
            ct[a[j]]+=1
    print(s)
    # print(r)
    for j in range(s):
        for k in range(3):
            print(l[j][k],end=' ')
        print("")
