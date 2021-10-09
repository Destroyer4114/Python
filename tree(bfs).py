n= int(input())



l=[[] for x in range(n+1)]
v=[[0]*(n+1)]

def bfs(node):
    v[node]=1
for i in range(n-1):
    p,q=map(int,input().split())
    l[p].append(q)
    l[q].append(p)
bfs(1)