for i in range(int(input())):
    x= int(input())
    if x%4==0:
        print("North")
    elif x%4==1:
        print("East")
    elif x%4==2:
        print("South")
    else:
        print("West")