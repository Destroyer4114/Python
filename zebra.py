for i in range(int(input())):
    n,mj=map(int,input().split())
    s= str(input())
    l=s[0]
    cl=0
    cll=0
 
    j=0
    for k in range(1,n):
        if s[k]!=l:
            cll=cl
            cl=k
            j+=1
            l=s[k]
            
        else:
            cl+=1
  
    if j<mj:
        print(-1)
    else:
        if mj%2==0:
            
            if s[0]==s[cl]:
                
                print(cl+1)
            else:
                print(cll+1)
        else:
            if s[0]!=s[cl]:
                print(cl+1)
            else:
                print(cll+1)
            


        




