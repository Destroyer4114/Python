from collections import Counter
for i in range(int(input())):
    n,x= map(int,input().split())
    a=list(map(int,input().split()))
    b=[k^x for k in a ]
    b.extend(a)
    na= Counter(a)
    nb= Counter(b)
    
    r=max(nb.values())
    mr= max(na.values())
    res =[]
    for key in nb:
        if nb[key] == r:
            res.append(key)

    
    m=0
    if x==0:
        r= mr
    elif r>mr:
        m=100000
        for i in range(len(res)):
            if nb[res[i]]- na[res[i]]<m:
                m=nb[res[i]]- na[res[i]]
    print(r,m)

    
    



    
    


    