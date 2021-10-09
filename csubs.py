t= int(input())
for i in range(t):
    n,k= map(int,input().split(' '))
    a= map(int,input().split(' '))
    def count(x):
        s=0
        s1 =0
        s2=0
        while x<n:
            s= s+1
            
