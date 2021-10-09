t= int(input())
for i in range(t):
    n,m,k= map(int,input().split())
    l=[int(x)for x in input().split()]
    b=[]
    s=0
    for j in range(1,n+1):
        if l.count(j)>1:
            s=s+1
            b.append(j)
    print(s,end=' ')        
    for i in range(s):
        print(b[i],end=' ')
    print(" ")
    
            


