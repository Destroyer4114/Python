for i in range(int(input())):
    l,r= map(int,input().split())
    k=int(r//3)-int((l-1)//3)
    # m=(r-l)%3
    # for j in range(1,m+1):
    #     if (l+j)%3==0:
    #         k+=1
    print(k)
