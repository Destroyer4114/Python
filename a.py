n = int(input())
l=[0]*(100000000)
for i in range(n):
    a,b= map(int,input().split(' '))
    l[a]=b
q= int(input())
for j in range(q):
    m = input().split()
    if len(m)==3:
        for k in range(int(m[0]),int(m[1])+1):
            l[k]= l[k]+int(m[2])
    else:
        s=l[int(m[0])]
        p=int(m[0])
        for k in range(int(m[0]),int(m[1])+1):
            if l[k]>s:
                p= k
                s=l[k]
        print(p)





    

    

