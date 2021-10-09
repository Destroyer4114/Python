for i in range(int(input())):
    n,d=map(int,input().split())
    p=[int(x) for x in input().split()]
    s=[int(x) for x in input().split()]
    
    m=[]
    for j in range(n):
        
        m.append(s[j]/p[j])
    ms= sorted(m,reverse=True)
    ps=[]
    ss=[]
    ex=[]
    add=[]
    s1=0
    s2=0
    for j in range(n):
        s2=s1
        w1=ms[j]

        w=m.index(w1)

        if w in ex:
            print("A")
            m[w]=0
            w=m.index(w1)
            add.append(ex[len(ex)-1])
            ex.pop()
            s1=s1+1
        
        
            
            
        ex.append(w)
        ps.append(p[w])
        ss.append(s[w])
    c=0
    s1=0
    sum1=0
    mon= d
    while  sum1 <n:
        mon= mon-ps[sum1]
        if mon>0:
            c= c+ss[sum1]
            s1=s1+1
        else:
            mon= mon+ps[sum1]
        sum1 = sum1+1
        if s1==2:
            break

        
    print(c)
    print(s,p,ss,ps,m,ms,ex)
        



