for i in range(int(input())):
    n= int(input())
    s= n%4
    if s==0 or s==1:
        print(n-s)
    elif s==2:
        print(n-1)
    else:
        print(n)