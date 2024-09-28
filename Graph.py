class Graph:
    def __init__(self):
        self.graph={}
        self.directed=False
    def AddVertex(self,Vertex):
        if Vertex not in self.graph:
            self.graph[Vertex]=[]
    def AddEdge(self,source,destination):
        self.AddVertex(source)
        self.AddVertex(destination)
        self.graph[source].append(destination)


        if not self.directed:
            self.graph[destination].append(source)
    def displayGraph(self):
        for Vertex in self.graph:

             print(f"{Vertex}:{self.graph[Vertex]}")
Gh=Graph()
Gh.AddEdge('A','B')
Gh.AddEdge('A','C')
Gh.AddEdge('A','D')
Gh.AddEdge('B','C')
Gh.AddEdge('C','D')
Gh.AddEdge('A','E')
print("Adjacency List")
Gh.displayGraph()

