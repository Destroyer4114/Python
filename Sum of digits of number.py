num = int(input("Enter a number:  "))
result = 0
hold = num
while num>0:
    i = num%10
    result = result + i
    num = int(num/10)
print("Sum of digits of",hold,"is",result)
