for i in range(int(input())):
    m,n,k=map(int,input().split())
    if m>n*k:
        print("YES")
    else:
        print("NO")