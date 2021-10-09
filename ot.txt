def find_shortest_path(graph, start, end, path =[]):
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
for i in range(int(input())):
    print("Case #"+str(i+1)+":",end=' ')
    s= list(str(input()))
    n=[0]*(26)
    for j in range(len(s)):
        n[ord(s[j])-65]+=1
    k= int(input())
    dic={'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [],'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}
    for j in range(k):
        l= list(str(input()))
        dic[l[0]].append(l[1])

    ss=list(set(s))
    # print(ss,n)
    c=[]
    for j in range(26):
        rr=0
        # print(ss[j])
        for f in range(len(ss)):
            r=find_shortest_path(dic,ss[f],chr(65+j), path =[])
            # print(ss[f],ss[j],r)
            
            if (r==None):
                rr=-1
                break
            
            else:
                rr += (len(r)-1)*( n[ord(ss[f])-65])
                
        c.append(rr)
    c= list(set(c))
    # print(c)
    c.sort()
    if c[0]==-1:
        c.remove(-1)
    if len(c)==0:
        print(-1)
    else:
        print(c[0])


        




        