for i in range(int(input())):
    n,d,h=[int(x) for x in input().split()]
    a=[int(x) for x in input().split()]
    s=0
    z=0
    for j in range(n):
        if a[j]>0:
            s= s+a[j]
        else:
            if s-d>0:
                s= s-d
            else:
                s=0
        if s>h:
            z=1
            break
    if z==1:
        print("YES")
    else:
        print("NO")