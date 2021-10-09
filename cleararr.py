t= int(input())
for i in range(t):
    n,k,x= map(int,input().split())
    a= list(map(int,input().split()))
    c=sum(a)
    a.sort(reverse=True)
    t1=0
    r=0
    while t1 ==0:
        if a[r]+a[r+1]>x and k>0:
            c=c-(a[r]+a[r+1])+x
            k= k-1
            r=r+2
        else:
            r=r+1
        if k==0:
            t1==1
            break
        if r>=n-1:
            t1==1
            break

        
    print(c)



    
