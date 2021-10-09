for i in range(int(input())):
    n,k,l=map(int , input().split())
    s= list(map(int , input().split()))
    c=s[n-1]
    s.sort(reverse=True)
    if n==1:
        print("Yes")
    else:
        if c== s[0] and c> s[1]:
            print("Yes")
        else:
            if k>0:
               
                c= c+ (int(l/k)*k)
                    
                if c> s[0]:
                    print ("Yes")
                else:
                    print("No")
            else:
                print("No")


