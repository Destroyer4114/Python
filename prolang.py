for i in range(int(input())):
    n= list(map(int,input().split()))
    s=0
    if{n[0],n[1]}=={n[2],n[3]}:
        s=1
    if{n[0],n[1]}=={n[4],n[5]}:
        s=2
    print(s)