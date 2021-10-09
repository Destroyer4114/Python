n=int(input())
l=[[] for x in range(n+1)]
v=[0]*(n+1)
print(l)
def dfs(node):
    v[node]=1
    print(node, end=' ')
    for i in l[node]:
        
        if v[i]!= 1:
            
            dfs(i)


for i in range(n-1):
    p,q=map(int,input().split())
    l[p].append(q)
    l[q].append(p)
print(l)

dfs(1)
