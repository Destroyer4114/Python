num = int(input("Enter number to find its factorial: "))
fact = 1
if num <0:
    print("Factorial of negative numbers doesn't exist")
elif num ==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact = fact*i
    print("Factorial of",num,"is",fact)
