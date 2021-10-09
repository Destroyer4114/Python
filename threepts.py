for i in range(int(input())):
    xa,ya = map(int,input().split())
    xb,yb = map(int,input().split())
    xc,yc = map(int,input().split())
    if (xa== xb):
        if (yc>=ya and yb>=ya) or((yc<=ya and yb<=ya)):
            if abs(yc-ya)>=abs(yb-ya):
                print("YES")
            else:
                print("NO") 
        else:
            print("NO") 
    elif (xc== xb):
        if (yc>=ya and yb>=ya) or((yc<=ya and yb<=ya)):
            if abs(yc-ya)>=abs(yb-ya):
                print("YES")
            else:
                print("NO") 
        else:
            print("NO") 
    elif (yb==yc):
        if (xc>=xa and xb>=xa) or((xc<=xa and xb<=xa)):
            if abs(xc-xa)>=abs(xb-xa):
                print("YES")
            else:
                print("NO")  
        else:
            print("NO") 
    elif (yb==ya):
        if (xc>=xa and xb>=xa) or((xc<=xa and xb<=xa)):
            if abs(xc-xa)>=abs(xb-xa):
                print("YES")
            else:
                print("NO") 
        else:
            print("NO") 
        
    else:
        print("NO") 
