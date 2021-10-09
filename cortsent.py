t= int(input())
for i in range(t):
    s=0
    l=input().split()
    k= int(l[0])
    for j in range(1,k+1):
        if (l[j].islower()==True and (l[j].count('n')==0 and l[j].count('o')==0 and l[j].count('p')==0 and l[j].count('q')==0 and l[j].count('r')==0 and l[j].count('s')==0 and l[j].count('t')==0 and l[j].count('u')==0 and l[j].count('v')==0 and l[j].count('w')==0 and l[j].count('x')==0 and l[j].count('y')==0 and l[j].count('z')==0 ))or (l[j].isupper()==True and (l[j].count('A')==0 and l[j].count('B')==0 and l[j].count('C')==0 and l[j].count('D')==0 and l[j].count('E')==0 and l[j].count('F')==0 and l[j].count('G')==0 and l[j].count('H')==0 and l[j].count('I')==0 and l[j].count('J')==0 and l[j].count('K')==0 and l[j].count('L')==0 and l[j].count('M')==0 )):
            continue
        else:
            s=1
            break
    if s==0:
        print("YES")
    else:
        print("NO")
