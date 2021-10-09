import collections
for i in range(int(input())):
    
    
    
    n= int(input())
    a=list(map(int,input().split()))
    data = collections.Counter(a)
    
    m=max(list(data.values()))
    if n<=2:
        print(0)
    elif(m==1):
        print(n-2)
    else:
        print(n-m)
#hogya maa ki chut
    

        
    

    

    

    
    
