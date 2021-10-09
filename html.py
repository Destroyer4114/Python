# cook your dish here
t= int(input())
for i in range(t):
    l= str(input())
    if l[0:2]=="</" and l[len(l)-1]=='>' and( (l[2:(len(l)-1)].islower()==True and l[2:(len(l)-1)].isalnum()==True) or l[2:(len(l)-1)].isdecimal()==True) :
        print("Success")
    # if l[0:2]=="</":
    #     print(1)
    # if  l[len(l)-1]=='>':
    #     print(2)
    # if l[2:(len(l)-1)].islower()==True:
    #     print(3)
    # if l[2:(len(l)-1)].isalnum()==True:
    #     print(4)
    # if l[2:(len(l)-1)].isdecimal()==True:
    #     print(5)
    
    else:
        print("Error")
    # print(">>",l[2:(len(l)-1)])