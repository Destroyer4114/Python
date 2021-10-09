for i in range(int (input())):
    n,k,s= map(int,input().split())
    s= (s- n**2)/(k-1)
    print(s)