for i in range(int(input())):
    p,a,b,c,x,y=map(int,input().split())
    s=0
    b+=x*a
    c+=y*a
    mi=min(b,c)
    ma=max(b,c)
    s=(p//mi)
    p=p-s*mi
    
    print(s)

