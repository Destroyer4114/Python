i= int(input("Enter a number: "))
for j in range(i,0,-1):
    print(" "*(i*2-j*2),end=' ')
    for k in range(1,j+1):
        print(k,end=' ')
    print()
