# cook your dish here
for i in range(int(input())):
    n,k=map(int,input().split())
    z= 2**n
    if k>=z/2:
        s= z*(z-1)
    else:
        s= 2*(z-1)*k
    print(s)