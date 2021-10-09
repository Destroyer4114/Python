for i in range(int(input())):
    a1,a2,a3,b1,b2,b3=map(int,input().split())
    if a1+a2+a3>b1+b2+b3:
        print(1)
    else:
        print(2)