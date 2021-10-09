for i in range(int(input(()))):
    n,m,x,y= map(int,input().split())
    d=0
    #for simple way
    d= (n+m-2)*x
    l= min(n,m)
    k= max(n,m)
    d= min(d,l*y+(k-l)*x)
    

    print(d)


    