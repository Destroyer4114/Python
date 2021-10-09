t= int(input())
for i in range(t):
    n,m= map(int,input().split())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    s=[]
    for j in range(m):
        
        if b[j]==1:
            s.append(0)
        else:
            
            x,y=b[j]-1,b[j]-1
            sr,sl=0,0
            while x+1<n:
                
                if a[x+1]==2:
                    sr=x+2-b[j]
                    break
                x= x+1
                # sr= sr+1
                
            while y-1>=0:
                
                if a[y-1]==1:
                    sl= b[j]-y
                    break
                y= y-1
                # sl= sl+1
                
            # if (sl+sr==n-1):
            #     s.append(-1)
            # else:
            #     s.append(max(sl,sr))
            if  sl==0 and sr==0:
                z=-1
            elif sr==0:
                z= sl
            elif sl==0:
                z= sr
            else:
                z= min(sl,sr)
            
            s.append(z)
    
    for _ in range(m):
        print(s[_],end=' ')
    print("")
    




