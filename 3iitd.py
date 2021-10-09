n,m= map(int,input().split())
a=[]
for i in range(n):
    a.append(list(str(input())))
    l=a[n]
    if l.count('S')==1:
        xs= l.index('S')
        ys =n
    if l.count('E')==1:
        xe= l.index('E')
        ye =n
def algo(x,y,a):
    if x>xe and y>ye:
        if a[x-1,y-1]!='X':
            x= x-1 
            y=y-1
        elif a[x-1,y]!='X':
            x= x-1 
            y=y
        elif a[x,y-1]!='X':
            x= x
            y=y-1
        
        

    elif x=xe and y>ye:
        if a[x-1,y-1]!='X':
            x= x-1 
            y=y-1
        elif a[x-1,y]!='X':
            x= x-1 
            y=y
        elif a[x,y-1]!='X':
            x= x
            y=y-1
    elif x<xe and y>ye:
        if a[x-1,y-1]!='X':
            x= x-1 
            y=y-1
        elif a[x-1,y]!='X':
            x= x-1 
            y=y
        elif a[x,y-1]!='X':
            x= x
            y=y-1
    elif x>xe and y=ye:
        if a[x-1,y-1]!='X':
            x= x-1 
            y=y-1
        elif a[x-1,y]!='X':
            x= x-1 
            y=y
        elif a[x,y-1]!='X':
            x= x
            y=y-1

    elif x=xe and y=ye:
        if a[x-1,y-1]!='X':
            x= x-1 
            y=y-1
        elif a[x-1,y]!='X':
            x= x-1 
            y=y
        elif a[x,y-1]!='X':
            x= x
            y=y-1
    elif x<xe and y=ye:
        if a[x-1,y-1]!='X':
            x= x-1 
            y=y-1
        elif a[x-1,y]!='X':
            x= x-1 
            y=y
        elif a[x,y-1]!='X':
            x= x
            y=y-1
    elif x>xe and y<ye:
        if a[x-1,y-1]!='X':
            x= x-1 
            y=y-1
        elif a[x-1,y]!='X':
            x= x-1 
            y=y
        elif a[x,y-1]!='X':
            x= x
            y=y-1
    elif x=xe and y<ye:
    elif x<xe and y<ye:

    

a=[]



