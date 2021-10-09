t= int(input())
for i in range(t):
    D,d,p,q= map(int,input().split())
    
    a=int(D/d)
    b= D%d  
    s= p*D + int(q*a*(a-1)*0.5*d) +q*a*b
    print(int(s))

