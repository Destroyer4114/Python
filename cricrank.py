for i in range(int(input())):
    l=[int(x) for x in input().split()]
    m=[int(x) for x in input().split()]
    sl=0
    sm=0
    if l[0]>m[0]:
        sl = sl+1
    else:
        sm=sm+1
    if l[1]>m[1]:
        sl = sl+1
    else:
        sm=sm+1
    if l[2]>m[2]:
        sl = sl+1
    else:
        sm=sm+1
    if sl>sm:
        print("A")
    else:
        print("B")

