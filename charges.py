t= int(input())
for i in range(t):
    n,k= map(int,input().split())
    s1=str(input())
    s2=' '
    s1= s2.join(s1)
    s= [int(x) for x in s1.split()]
    q= [int(x) for x in input().split()]
    
    
    

    d=0
    l=s[0]
    for j in range(1,n):
        if s[j]==l:
            d= d+2
        else:
            d=d+1
        l=s[j]
    for j in range(k):
        if q[j]<n:
            if s[q[j]-1]==s[q[j]]:
                d= d-1
            else:
                d=d+1
        
        if q[j]>=2:
            
            if s[q[j]-1]==s[q[j]-2]:
                d= d-1
            else:
                d=d+1

        if s[q[j]-1]==1:
            s[q[j]-1]=0
        else:
            s[q[j]-1]=1
        print(d)


