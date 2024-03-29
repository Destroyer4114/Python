# Python3 program for above approach

# Graph class represents a undirected graph
# using adjacency list representation
class Graph:
	
	def __init__(self, V):

		# No. of vertices
		self.V = V

		# Pointer to an array containing
		# adjacency lists
		self.adj = [[] for i in range(self.V)]

	# Function to return the number of
	# connected components in an undirected graph
	def NumberOfconnectedComponents(self):
		
		# Mark all the vertices as not visited
		visited = [False for i in range(self.V)]
		
		# To store the number of connected
		# components
		count = 0
		
		for v in range(self.V):
			if (visited[v] == False):
				self.DFSUtil(v, visited)
				count += 1
				
		return count
		
	def DFSUtil(self, v, visited):

		# Mark the current node as visited
		visited[v] = True

		# Recur for all the vertices
		# adjacent to this vertex
		for i in self.adj[v]:
			if (not visited[i]):
				self.DFSUtil(i, visited)
				
	# Add an undirected edge
	def addEdge(self, v, w):
		
		self.adj[v].append(w)
		self.adj[w].append(v)
		
# Driver code	


# This code is contributed by rutvik_56



for i in range(int(input())):
    n= int(input())
    w= list(map(int, input().split()))
    l=[]
    s=0
    for j in range(n):
        for k in range(j):
            if k-j!=w[k]-w[j]:
                l.append([k,j])
                s+=1
                
    if __name__=='__main__':
        g = Graph(n)
        for j in range(s):
            g.addEdge(l[j][0],l[j][0])
        print(g.NumberOfconnectedComponents())
    

