for i in range(int(input())):
    a=[int(x) for x in input().split()]
    if a[0]+a[2]+a[4]+a[6]+a[8]>a[1]+a[3]+a[5]+a[7]+a[9]:
        print(1)
    elif a[0]+a[2]+a[4]+a[6]+a[8]<a[1]+a[3]+a[5]+a[7]+a[9]:
        print(2)
    else:
        print(0)