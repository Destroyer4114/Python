i = int(input("Enter a number: "))
j= 2*i-1
for k in range(1,j+1,2):
    print(" "*int((j-k)/2),end=' ')
    print("*"*k,end=' ')
    print(" "*int((j-k)/2))      
for k in range(j-2,0,-2):
    print(" "*int((j-k)/2),end=' ')
    print("*"*k,end=' ')
    print(" "*int((j-k)/2))
