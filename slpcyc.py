for i in range(int(input())):
    l,h=map(int,input().split())
    s= [int(x) for x in list(input())]
    s1=0
    s2=0
    
    for j in range(l):
        
        if s[j]==0:
            s1=s1+1
            print("->",s1,h)
            if s1>=h:
                s2=1
                break
        else:
            k=h
            if s1!=0:
                h= 2*(k-s1)
                s1=0
            
            
    if s2==0:
        print("NO")
    else:
        print("YES")




    