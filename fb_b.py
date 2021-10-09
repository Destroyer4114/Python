for i in range(int(input())):
    print("Case #"+str(i+1)+":",end=' ')
    n= int(input())
    l=[]
    m=[]
    for j in range(n):
        l.append(list(str(input())))
    s=[]
    for j in range(n):
        sx=0
        so=0
        mc=[]
        for k in range(n):
            if l[j][k]=='.':
                sx=sx+1
                mc.append([k,j])
                
            elif l[j][k]=='O':
                so=so+1
        if so==0:
            s.append(sx) 
            if sx==1:
                m.extend(mc) 
             
    
    for k in range(n):
        sx=0
        so=0
        bc=0
        
        for j in range(n):
            if l[j][k]=='.':
                sx=sx+1
                if m.count([k,j])!=0:
                    bc=1
                
            elif l[j][k]=='O':
                so=so+1
        if so==0:
            if sx==1 and bc==1:
                continue
            else:
                s.append(sx)  

            
    if len(s)==0:
        print("Impossible")   
    else:
        s.sort()
        sc= s.count(s[0]) 
        print(s[0],sc)
            