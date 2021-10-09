t= int(input())
l=[]
for i in range(t):
    a,b,c,d,e= map(int, input().split(' '))
    if a>=c or a >=e:
        l.append(-1)
    else:
        l.append(1)
    if c>=a*b or (c>=e and b<=d) or(c>=e and int(c/e)*d>b )  :
        l.append(-1)
    else:
        l.append(b)
    if e>=a*d or (e>=c and b>=d)or(c<=e and int(e/c)*b>d ):
        l.append(-1)
    else:
        l.append(d)
    for j in range(3):
        print(l[j] )
        
    