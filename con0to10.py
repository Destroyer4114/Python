t= int(input())
n= int(input())
for i in range(t):
    s=0
    m= int(input())
    if n!=32:
        i=0
        while m>0:
            s=s+ (m%10)*((n)**i)
            m= int(m/10)
            i=i+1
        print(s)
    

    