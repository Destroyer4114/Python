from math import sqrt
n= int(input())
l=[2,3]
ss=1
sn=0
for i in range(5,n):
    prime_flag = 0
    if(i> 1):
        for j in range(2, int(sqrt(i)) + 1):
            if (i % j == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            l.append(i)
            ss+=1
        if l[ss]-l[ss-1]==2:
            sn+=1
print(sn)
        
            

	





