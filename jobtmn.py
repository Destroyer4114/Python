for i in range(int(input())):
    n,m,l=map(int,input().split())
    a=[]
    d=[0]*(n+1)
    for j in range(m):
        # a.append([int(x) for x in input().split()])
        a=[int(x) for x in input().split()]
        for k in range(1,a[0]+1):
            b1= a[k]
            d[b1]=j+1

    # print (d)

    b=[int(x) for x in input().split()]
    for j in range(l):
        a1= b[j]
        # print(a1)
        # print(b)
        
        b[j]=d[a1]
    
    # for j in range(m):
        
    #     for k in range(2,a[j][0]+1):

            
    #         while b.count(a[j][k])>0:
                
    #             f=b.index(a[j][k])
    #             b[f]=a[j][1]
    z=b[0]
    s=1
    for i in range(1,l):
        if b[i]==z:
            continue
        else:
            z= b[i]
            s= s+1
    print(s)


    


        