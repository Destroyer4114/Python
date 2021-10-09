t= int (input())
for i in range(t):
    l = list(map(int, input().split()))
    m= max(l)
    if l[2]== m:
        print("Alice")
    elif l[1]==m:
        print("Bob")
    else:
        print("Draw")