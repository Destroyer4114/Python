m= int(input("Number of rows:"))
n= int(input("Number of columns:"))
while 1<= m <= 10**9 and 1<= n <= 10**9:
    if m%2!=0:
        if n%2!=0:
            z= ((m+1)/2)+((n-1)*m/2)
        else:
            z= m*n/2
    else:
        if n%2!=0:
            z= m*n/2
        else:
            z= m*n/2
    print(z,"is the maximum number of red flags")
    break

    

    
