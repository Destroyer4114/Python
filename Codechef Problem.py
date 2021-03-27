#Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges).
#For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an attempted transaction.
x=int(input("Enter the amount Pooja wants to withdraw: $"))
y= float(input("Enter the balance of pooja: $"))
y = round(y,2)
if 0<x<= 2000 and 0<= y<=2000:
    if x%5==0:
        if x-0.5>=y:
            z = y-x-0.5
            z= round(z,2)
            print("$",y,"withdrawn successfully")
            print("Balance : $",z)
        else:
            print("Insufficient Balance")
        
    else:
        print("Entered amount can't be withdrawn. Transaction aborted.")
else:
    print("Figures are out of limit")
