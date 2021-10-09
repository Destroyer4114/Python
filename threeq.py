for i in range(int(input())):
    a= list(map(int , input().split()))
    b= list(map(int , input().split()))
    if sum(a)== sum(b):
        print("Pass")
    else:
        print("Fail")