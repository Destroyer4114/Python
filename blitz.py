t= int(input())
for i in range(t):
    n,a,b= map(int, input().split())
    print(360-a-b+n*2)