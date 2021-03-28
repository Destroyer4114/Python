def fb(n):
  if n < 2:
    return n

  return fb(n - 1) + fb(n - 2)
n=int(input("Enter value of n: "))
print("Value of nth term of fibbonaci sequence is: ",fb(n))
