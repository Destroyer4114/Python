n= int(input())
l=[]
for i in range(n):
    j= int(input())
    l.append(j)
l.sort(reverse=True)
s=0
i=2
while n>=3:
    s= s+l[i]
    i = i+3
    n= n-3
print(sum(l)-s)
