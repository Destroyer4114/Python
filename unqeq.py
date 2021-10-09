for i in range(int(input())):
    n=int(input())
    if n%4==0:
        print("YES")
        for j in range(1,int(n/4)+1):
            print(j,end=' ')
        for j in range(1,int(n/4)+1):
            print(n-j+1,end=' ')
        print()
        for j in range(int(n/4)+1,int(n/2)+1):
            print(j,end=' ')
        for j in range(int(n/4)+1,int(n/2)+1):
            print(n-j+1,end=' ')
        print()
    else:
        print("NO")

        


