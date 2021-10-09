t= int(input())
for i in range(t):
    n= int(input())
    l=[]
    m=[]
    for i in range(3*n):    
        a,b= input().split()
        if a in l:
            m[l.index(a)]+=int(b)
        else:
            l.append(a)
            m.append(int(b))
    
    r=''.join(str(e)+' ' for e in sorted(m))
    print(r)