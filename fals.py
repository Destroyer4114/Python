t= int(input())
for i in range(t):
    l= str(input())
    n= int(len(l))
    if l[0]=='1':
        print('10'+ l[1:n])
    else:
        print('1'+l)