# cook your dish here
for i in range(int(input())):
    n,p,k=map(int,input().split())
    a= p%k
    b= int((n-1)/k)
    c= b*k
    s=b*a
    if c+a-1<n:
        s= s+a
    else:
        s= s+(n-c)
    
    
        
    s= s+ ((p-a)/k)+1
    print(int(s))


        

