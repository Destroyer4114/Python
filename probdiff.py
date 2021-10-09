for i in range(int(input())):
    l=[int(x) for x in input().split()]
    a= list(set(l))
    if len(a)==4 or len(a)==3:
        print(2)
    elif len(a)==2:
        m=l.count(a[0])
        if m==1 or m==3:
            print(1)
        else:
            print(2)
    else:
        print(0)

    

