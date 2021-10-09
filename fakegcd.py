for i in range(int(input())):
    n= int(input())
    e=2
    o=1
    for j in range(1,n+1):
        if j%2==0:
            print(e,end=' ')
            e+=2
        else:
            print(o,end=' ')
            o+=2
    print()