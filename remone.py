for i in range(int(input())):
    n= int(input())
    a= list(map(int,input().split()))
    b= list(map(int,input().split()))
    a.sort()
    b.sort()
    # if b[0]-a[0]==b[1]-a[1] and b[0]-a[1]==b[1]-a[2]:
    #     print(min(b[0]-a[0],b[0]-a[1]))
    # else:
        

        # if b[0]-a[0]==b[1]-a[1]:
        #     print(b[0]-a[0])
        # else:
        #     print(b[0]-a[1])
  
    if n==2:
        if b[0]-a[0]<0:
            print(b[0]-a[1])
        elif b[0]-a[1]<0:
            print(b[0]-a[0])
        else:
            print(min(b[0]-a[0],b[0]-a[1]))
        
        
    elif (b[0]-a[0]==b[1]-a[1] and b[0]-a[1]==b[1]-a[2]) :
        print(min(b[0]-a[0],b[0]-a[1]))
    else:
        if( b[0]-a[0]==b[1]-a[1] or b[0]-a[0]== b[1]-a[2] )and b[0]-a[0]>0 :
            print(b[0]-a[0])
        elif b[0]-a[1]==b[1]-a[2] and b[0]-a[1]>0:
            print(b[0]-a[1])