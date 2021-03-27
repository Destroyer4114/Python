import random
x= random.randrange(100)
y= int(input("Guess a number in between 0 to 100:"))
while x!=y:
    if x>y:
        print("Too Low")
    else:
        print("Too High")
    y= int(input("Guess a number in between 0 to 100:"))
if x==y:
    print("Congo, U guessed the number")
