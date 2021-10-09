    for i in range(int(input())):
        a,b,c=map(int,input().split())
        s= min(a,b,c)
        print(a+b+c-s)