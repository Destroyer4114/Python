for i in range(int(input())):
    n,q=map(int,input().split())
    a=[int(x) for x in input().split()]
    e=[]
    o=[]
    for i in range(n):
        if a[i]%2==0:
            e.append(i+1)
        else:
            o.append(i+1)

    # print(e,o)
    for i in range(q):
        l,r=map(int,input().split())
        se=0
        so=0
        for j in range(len(e)):
            if l<=e[j]<=r:
                se= se+1
        for j in range(len(o)):
            if l<=o[j]<=r:
                so= so+1
        # print(">",se,so)
        s= (((se)*(se-1)*(se-2))/6 ) +(((se)*(so)*(so-1))/2)
        print(s)


