t = int(input())
for i in range(1,t+1):
    n, m = [int(x) for x in input().split()]
    l = list(int(x) for x in input().split())
    if 1<=len(l)<= n and 1<=n<= 10**5 and 1<=m<= 10**5:
        for j in range(1,m+1):
            if l.count(j)==0:
                print("YES")
        print("NO")
