for i in range(int(input())):
    x,y=map(int,input().split())
    if 6-(x+y)>0:
        print((6-(x+y))/6)
    else:
        print(0)