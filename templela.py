for i in range(int(input())):
    n=int(input())
    h= list(map(int,input().split()))
    r=1
    if n%2!=0:
        for i in range(0,int(n/2)+1):
            if h[i]!=i+1:
                r=0
                break
        for i in range(n-1,int(n/2),-1):
            if h[i]!=i+2-n:
                r=0
                break
    else:
        r=0
    if r==0:
        print("no")
    else:
        print("yes")


        
        