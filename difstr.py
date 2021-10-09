t= int(input())
for i in range(t):
    n= int(input())
    l=str()
    for j in range(n):
        
        a= list(str(input()))
        if a[j]=='1':
            l += '0'
        else:
            l += '1'
        
    print(l)
