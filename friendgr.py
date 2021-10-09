def ct(c):
    while s[c]=='0':
        c= c-1
    c= c+k
    
for i in range(int(input())):
    n,k= map(int,input().split())
    s= list(str(input()))
    s1=0
    c=0
    cc=0
    p=0
    while c<n:
        if s[c]=='1':
            if p==0:
                p=1
                s1=s1+1
                c=c+k
                ct(c)
                
            if p==1:
                c=c+k
                ct(c)
                
        else:
            if p==0:
                c=c+1
            elif c<n-1:
                if s[c+1]=='1':
                    c=c+k-1
                    ct(c)
                else:
                    c=c+2
                    p=0
    print(s1)
                

                





