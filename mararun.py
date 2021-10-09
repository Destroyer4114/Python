t= int(input())
for i in range(t):
    D,d,A,B,C = map(int,input().split(' '))
    s=0
    if d*D>=10:
        s=A
    if d*D>=21:
        s=B
    if d*D>=42:
        s=C
    print(s)
