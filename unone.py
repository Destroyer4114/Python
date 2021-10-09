t= int(input())
for i in range(t):
    n= int(input())
    k=input()
    l=[int(x) for x in k.split() ]
    
    if l[n-1]%2!=0:
        print(k)
    else:
        a=0
        while l[a]%2==0 and a<n-1:
            a= a+1
        b= l[a]
        l.pop(a)
        l.append(b)
        for j in range(n):
            print(l[j], end=' ')
        print("")

