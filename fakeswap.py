for i in range(int(input())):
    n= int(input())
    s= str(input())
    p= str(input())
    s0=0
    s1=0
    for j in range(n):
        if p[j]=='1':
            s1+=1
        else:
            s0+=1
    if s==p:
        print("YES")
        break
    if s1==0 or s0==0:
        print("NO")
    else:
        print("YES")