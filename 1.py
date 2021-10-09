from collections import *
for i in range(int(input())):
    n= int(input())
    a= list(map(int,input().split()))
    b= list(map(int,input().split()))
    a.sort()
    b.sort()
    x= float("inf")
    m= defaultdict(int)
    for i in range(n-1):
        m1= b[i]- a[i]
        m2 =  b[i]- a[i+1]
        if m1!=m2:
            if m1>0:
                m[m1]+=1
            if m2>0:
                m[m2]+=1
        else:
            if m1>0:
                m[m1]+=1
    for i in m.keys():
        if m[i]== n-1:
            x =min(x,i)
        print(x)
 

    # if n==2:
    #     if b[0]-a[0]<0:
    #         print(b[0]-a[1])
    #     elif b[0]-a[1]<0:
    #         print(b[0]-a[0])
    #     else:
    #         print(min(b[0]-a[0],b[0]-a[1]))
        
        
    # elif (b[0]-a[0]==b[1]-a[1] and b[0]-a[1]==b[1]-a[2]) :
    #     print(min(b[0]-a[0],b[0]-a[1]))
    # else:
    #     if( b[0]-a[0]==b[1]-a[1] or b[0]-a[0]== b[1]-a[2] )and b[0]-a[0]>0 :
    #         print(b[0]-a[0])
    #     elif b[0]-a[1]==b[1]-a[2] and b[0]-a[1]>0:
    #         print(b[0]-a[1])
        
