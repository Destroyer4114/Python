for i in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        s= str(input())
        for j in range(m):
            if s[m]=='1':
                l.append([i+1,j+1])
    n=[0]*(n+m-1)
    ll = len(l)
    for i in range(ll):
        for j in range(i+1,ll):
            c=abs(l[i][0]-l[j][0])+abs(l[i][1]-l[j][1])
            n[c]+=1
    print(n)
            