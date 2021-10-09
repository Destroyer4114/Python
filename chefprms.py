# cook your dish here
p=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
k=[0]*201
l=[]

for i in range(len(p)):
    for j in range(len(p)):
        r=p[i]*p[j]
        if r<=200 and i!=j:
            l.append(r)
            k[r]+=1
# print(l,k)
for i in range(int(input())):
    a=0
    n= int(input())
    for j in range(len(l)):
        if n>l[j]:
            if k[n-l[j]]>0:
                a=1
               
                break
    if a==1:
        print("YES")
    else:
        print("NO")
    
        