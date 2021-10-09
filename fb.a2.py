for i in range(int(input())):
    print("Case #"+str(i+1)+":",end=' ')
    s= list(str(input()))
    n=[0]*(26)
    for j in range(len(s)):
        n[ord(s[j])-65]+=1
    k= int(input())
    dic={'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0,'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for i in range(k):
        l= list(str(input()))
        dic[l[0]]=l[1]
    cm=0
    ce=0
    de=0
    dec=0
    for j in range(26):
        if cm< n[j]:
            cm=n[j]
            ce=chr(65+j)
        if n[j]!=0 and dic[chr(65+j)]==0:
    
            de+=1
            dec=chr(65+j)
    sn= sum(n)
    ss= list(set(s))
    # print(ss,dec)
    c=0
    if de>=2:
        print(-1)
    elif de==1:
        for j in range(len(ss)):
            if ss[j]==dec:
                continue
            else:
                lr=ss[j]
                r=dic[ss[j]]
                # print(lr,r)
                while r!= dec:
                    lr=r
                    c= c+ n[ord(r)-65]
                    r=dic[r]
                    if lr== dic[r]:
                        de=-1
                    if r==0:
                        break
                
                if r==0:
                    de=2
                    break
                else:
                    # print(c,ord(lr)-65)
                    c= c+ n[ord(lr)-65]
                
        if de==2:
            print(-1)
        else:
            print(c)
    else:
        for j in range(len(ss)):
            if ss[j]==ce:
                continue
            else:
                
                lr=ss[j]
                r=dic[ss[j]]
                while r!= ce:
                    
                    lr=r
                    c= c+ n[ord(r)-65]
                    r=dic[r]
                    if r==0 or r==dic[dic[r]]:
                        break
                
                if r==0 or r==dic[dic[r]]:
                    de=de+1
                    dec=lr
                else:
                    c= c+ n[ord(lr)-65]
        if de==2:
            print(-1)
        elif de==1:
            ss= list(set(s))
            for j in range(len(ss)):
                if ss[j]==dec:
                    continue
                else:
                    lr=ss[j]
                    r=dic[ss[j]]
                    while r!= dec:
                        lr=r
                        c= c+ n[ord(r)-65]
                        r=dic[r]
                        if r==0 or r==dic[dic[r]]:
                            break
                    if r==0 or r==dic[dic[r]]:
                        de=2
                        break
                    else:
                        c= c+ n[ord(lr)-65]

            if de==2:
                print(-1)
            else:
                print(c)

        else:
            print(c)

        

        
                    




    #dictionary mien hi modifications kr deni hai rtaaki har ek case ka ho ke iske lie hai hi nhi aur iske lie  yeh hai 2 ke lie yeh and 3 ke lie yeh and so on if it goes to rev then tooo f u bitch krdio kal laude


    



#     dic={'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
#  'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 
# 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}