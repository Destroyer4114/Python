for i in range(int(input())):
    n,m,x=map(int,input().split())
    a=[int(x) for x in input().split()]
    d={}
    for  j in range(n):
        d[a[j]]=j+1
    a.sort(reverse=True)
    s1=0
    l=[]
 
    while a[s1]>=m:
        l.append(d[a[s1]])
        if s1<n-1:
            # print("a")
            s1=s1+1
        else:
            break

    # print( s1,len(l))
    if s1<x:
        
        for k in range(s1,x):
            l.append(d[a[k]])
        

    l.sort()
    print(len(l), end=' ')
    for j in range(len(l)):
        print(l[j],end=' ')
    print()
    
    

