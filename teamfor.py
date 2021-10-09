for i in range(int(input())):
    n= int(input())
    s= list(str(input()))
    t= list(str(input()))
    s1,s2,s3,s4=[0,0,0,0]
    for j in range(n):
        if (s[j]=='1' and t[j]=='1'):
            s1+=1
        elif s[j]=='0' and t[j]=='1':
            s2+=1
        elif s[j]=='1' and t[j]=='0':
            s3+=1
        elif s[j]=='0' and t[j]=='0':
            s4+=1
    r=0
    if s2>s3:
        r= r+s3
        
    else:
        r= r+ s2
    s4= s4 +abs(s2-s3)
    if s1<s4:
        r+= s1
    else:
        r+= s4 +int((s1-s4)/2)
    print(r)


    
