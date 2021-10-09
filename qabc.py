def add(a,i,b):
    z= b[i]-a[i]
    a[i]+=z
    a[i+1]+=z*2
    a[i+2]+=z*3

for i in range(int(input())):
    r=1
    n= int(input())
    a= list(map(int,input().split()))
    b= list(map(int,input().split()))
    for j in range(n-2):
        if a[j]<b[j]:
            add(a,j,b)
        else:
            r=0
            break
    if a!=b:
        r=0
    if r==0:
        print("NIE")
    else:
        print("TAK")


