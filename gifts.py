t= int(input())
for i in range(t):
    n,k= map(int,input().split())
    a=[int(x) for x in input().split()]
    a= sorted(a)
    a.reverse()
    
    s1=0
    s2=a[n-1]
    for i in range(0,n-2,2):
        s1 = s1 +a[i]
        s2= s2 +a[i+1]
    print(max(s1,s2))
