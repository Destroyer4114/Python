n,m= map(int,input().split())
x,y,z= map(int,input().split())
l=[]
a=[]
b=[]
for i in range(n):
    l=[int(x) for x in input().split()]
    a.append(x*l[0]+z*l[2]+y*l[1])
    

c= sorted(a)


s=0
m= m-c[0]



while m>=0:
    b.append(a.index(c[s]))
    c[s]=0
    s= s+1
    m= m- c[s]
    
    
print(s)
for i in range(s):
    print(b[i]+1,end=' ')

