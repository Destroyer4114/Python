
for i in range(int(input())):
    n= int(input())
    l=2
    s=1
    while(n>1):
        if(n%2==0):
            n=int(n/2)
            if(l==1):
                s+=1
                l=0
        else:
            n= n-1
            l=1
            s+=1
    if (s%2==0):
        print("Bob")
    else:
        print("Alice")
            


    