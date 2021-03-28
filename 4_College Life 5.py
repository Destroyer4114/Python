t = int(input())

for i in range(1,t+1):
    b=0
    n, m = [int(x) for x in input().split()]
    f = list(int(x) for x in input().split())
    c = list(int(x) for x in input().split())
    l = f +c
    j= sorted(l)
    
    for k in range(0,n+m):
        a= j[k]
        
        if c.count(a)==0:
           
            if b%2==0:
                b=b
                
            else:
                b = b+1
           
            
        else:
            
            if b%2==0:
                b = b+1
            else:
                b= b
            
    print(b)
            
