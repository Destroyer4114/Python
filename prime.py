n= int(input())
f=0
l=[2]
b=[]
p=2
for i in range(3,n+1):
    f=0
    for j in range(2,int(i/2)+1):
        if i%j==0:
            f=1
            break
        
    if f==0:
        l.append(i)
        b.append(i*p)
        
print(l)
print(b)