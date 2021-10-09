for t in range(int(input())):
    print("Case #"+str(t+1)+":")
    n= int(input())
    l=[""*n]*n
    
    i= str(input())
    o= str(input())
    
    
    
    for j in range(n):
        for k in range(j,-1,-1):
            if j==k:
                l[j]= l[j]+'Y'
            else:
                if o[k+1]=='Y' and i[k]=='Y' and l[j][0]=='Y':
                    l[j]= 'Y'+l[j]
                else:
                    l[j]= 'N'+l[j]
        for k in range(j+1,n):
            if o[k-1]=='Y' and i[k]=='Y' and l[j][k-1]=='Y':
                l[j]= l[j] +'Y'
            else:
                l[j]= l[j] +'N'
                


            
            
    for j in range(n):
        print(l[j])
