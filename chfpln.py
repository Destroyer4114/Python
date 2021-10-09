for i in range(int(input())):
    n= int(input())
    s=0
    l=[ int(x) for x in input().split()]
    z=[0]*(10**5)
    # q=set(l)
    # r=list(q)
    for j in range(n):
        if z[l[j]-1]<l[j]-1:
             z[l[j]-1]= z[l[j]-1]+1
    print(sum(z))



    # for j in q:
    #     if l.count(j)>j-1:
    #         s=s+j-1
    #     else:
    #         s= s+l.count(j)



    # q=[]
    # r=[]
    # l=[]
    # for j in range(n):
    #     if l[j] not in q:
    #         q.append(l[j])
    #         r.append(l.count(l[j]))
    # for j in range(len(q)):
    #     if r[j]>q[j]-1:
    #         s=s+q[j]-1
    #     else:
    #         s= s+r[j]
    # print(s)

