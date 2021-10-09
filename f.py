n= int(input())
l=[int(x) for x in input().split(' ')]
a=[]
b=[]
for i in range(n):
    s=0
    if l[i] not in a:
        a.append(l[i])
        s=1

    
    for j in range(1,int(l[i]/2)+1):
        if j not in a and l[i]%j==0:
            s= s+1
            a.append(j)
    b.append(s)
for k in range(len(b)):
    print(b[k],end=' ')