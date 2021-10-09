for i in range(int(input())):
    n= int(input())
    a= list(map(int,input().split()))
    e=0
    o=0
    ee=[]
    oo=[]
    for j in range(n):
        if a[j]%2==0:
            e+=1
            ee.append(a[j])
        else:
            o+=1
            oo.append(a[j])
    if e>0 and o>0:
        t= max(o,e)
        l= min(o,e)
        if t==o:
            for j in range(l,t):
                print(oo[j],end=' ')

        for j in range(l):
            print(oo[j],ee[j],end=' ')
        if t==e:
            for j in range(l,t):
                print(ee[j],end=' ')    
        print()
    else:
        print(-1)
        

