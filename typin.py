for i in range(int(input())):
    fr=0
    n= int(input())
    dic={}
    ll=[]
    for j in range(n):
        r=0
        l='A'
        s= str(input())
        if s in ll:
            r=dic[s]/2
            fr+=r
            continue

        for k in range(len(s)):
            if s[k]=='d' or s[k]=='f':
                if l=='d' or l=='f':
                    r+=4
                else:
                    r+=2
            
            if s[k]=='j' or s[k]=='k':
                if l=='j' or l=='k':
                    r+=4
                else:
                    r+=2
            
            l=s[k]
            # print("-->",r,s[k],l)
            
        fr+=r
        dic[s]=fr
        ll.append(s)
        # print("->",fr,r)
    print(int(fr*10))

