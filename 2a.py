n= int(input())
a={}
s=[]
r1=0
s1=""
for i in range(n):
    c,b=input().split()
    b= int(b)
    if c in a:
        s[a[c]]+=b
    else:
        s.append(b)
        a[c]=(len(s)-1)
    if s[a[c]]>r1:
        r1=s[a[c]]
        s1= c
    print(s1)

    

