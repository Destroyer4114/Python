t = int(input())
while 1<= t<= 10**5:
    for i in range(1,t+1):
        n, k = [int(a) for a in input().split()]
        j = n%k
        while 3<= k <= 10**9 and 3<= n<= 10**9:
            if j ==0:
                d = int(n/k)
                x = k
            else:
                d = int(n/k)+1
                x = n%k
            print(d,x)
            break
    break

    
