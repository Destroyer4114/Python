num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
op = input("Choose any one of the operators(+,-,/,*): ")

if op == "+":
    result = num1 + num2
elif op == "-":
    if num1 > num2:
        result = num1 - num2
    else:
        result = num2 - num1
elif op == "*":
    result = num1*num2
elif op == "/":
    if num2 == 0:
        result = " Division by 0 not possible"
    else : result = num1/num2
else:
    result = "Operator not valid"
print("Your result is",result)
