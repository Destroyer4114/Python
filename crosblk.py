for i in range(int(input())):
    n= int(input())
    b= list(map(int, input().split()))
    a= sorted(b,reverse=True)
    
    # print(a,b)
 
    if a[0]!=b[0]:
        print(-1)
    else:
        c=1
        sc=1
        s=1
        
        while sc<n-1:

            if b[sc]!=a[c]:
                a.remove(b[sc])
                sc=sc+1
               
            else:
                c=c+1
                
                if a[c]!=a[c-1]:
                    
                    s=s+1
                sc=sc+1
        print(s)
                



        


