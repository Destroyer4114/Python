for i in range(int(input())):
    n= int (input())
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    for i in range(n-1,0,-1):
        for j in range(i):
            if a[i][j]< a[i][j+1]:
                a[i-1][j]+=a[i][j+1]
            else:
                a[i-1][j]+=a[i][j]
    print(a[0][0])


    

        

