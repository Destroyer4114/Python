i = int(input("Enter a number: "))
j = 2*i -1
for k in range(1,j+1,2):
    print(" "*int(3*i-k),end=' ')
    for l in range(int((k+1)/2),1,-1):
        print(l,end=' ')
    for l in range(1,int((k+3)/2)):
        print(l,end=' ')     
    print(" "*int((j-k)/2))
