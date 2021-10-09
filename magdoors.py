for i in range(int(input())):
    s=str(input())
    ct=0
    for i in range(len(s)):
        if ct%2==0:
            if s[i]==0:
                ct+=1
        else:
            if s[i]==1:
                ct+=1
    print(ct)
