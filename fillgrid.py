for i in range(int(input())):
    n= int(input())
    if n%2==0:
        for j in range(n):
            for k in range(n):
                print(-1, end='')
            print()
    else:
        for j in range(n):
            for k in range(n):
                if (j==k):
                    print(-1,end='')
                else:
                    print(1, end='')
            print()
