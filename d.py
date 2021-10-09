n= int(input())
l=[0]
for i in range(n):
    m=input().split(' ')
    if int(m[0])==1:
        l =[j+int(m[2]) for j in l[0:int(m[1])]]
        '''for j in range(int(m[1])):
            l[j]= l[j]+int(m[2])'''
    elif int(m[0])==2:
        l.append(int(m[1]))
    else:
        l.pop()
    print(sum(l)/len(l))



