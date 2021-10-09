
l=[0]*100001
for a in range(1,100000+1):
    for b in range(a,100000+1,a):
        if(b%a==0):
            for c in range(a,100000+1,b):
                if c%b==a:
                    z= max(a,b,c)
                    l[z] += 1

file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)
file1.close()
  
# Append-adds at last
file1 = open("myfile.txt", "a")  # append mode
file1.write(str(l))
file1.close()
  
# for i in range(int(input())):
#     s=0
#     n= int(input())
#     for j in range(2,n+1):
#         s= s+l[j]
#     print(s)
    
    
    
    
