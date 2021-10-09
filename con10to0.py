t= int(input())
n= int(input())
for i in range(t):
    s=""
    m= int(input())
    while m>0:
        s= str(m%n)+s
        m= int(m/n)
    print(s)
        
    