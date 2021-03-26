num = int(input("Enter number to check whether it is prime or not: "))
if num >3:
    for i in range(2,int((num+2)/2)):
        if num%i == 0:
            nof = 1
            break
        else:
            nof = 0
    if nof == 1:
        print(num, "is not a prime number")
    else:
        print(num , "is a prime number")
elif num == 2:
    print(num,"is a prime number")
elif num == 3:
    print(num,"is a prime number")
else:
    print("Number entered is <= 1,Try again")
