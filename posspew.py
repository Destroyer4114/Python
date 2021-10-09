for i in range(int(input())):
    n,k= map(int,input().split())
    a= list(map(int,input().split()))
    ll=[]
    l='1'
    s=0
    rs=0
    ss=0
    for j in range(n):
        if a[j]==0:
            if l=='1':
                l='0'
                s=1
            else:
                s+=1
        else:
            if l=='0':
                ll.append(s)
                s=0
                l='1'
        rs+=a[j]
    rs+=2*k*n
    if a[0]==0 and a[n-1]==0:
        if len(ll)>0:
            ll[0]+=s
        else:
            ll.append(s)
    # print(ll)
    for j in range(len(ll)):
        if ll[j]%2!=0:
            t= (ll[j]+1)/2
            if t>k:
                rs=rs-((ll[j]+2)*2*k)+2*k*(k+1)
            else:
                rs=rs-((ll[j]+2)*2*k)+2*t*(t+1)
        else:   
            t= ll[j]/2
            if t>k:
                rs=rs-((ll[j]+2)*2*k)+2*k*(k+1)
            else:
                rs=rs-((ll[j]+2)*2*k)+2*t*(t+1)
    print(rs)


            
            
        
    


