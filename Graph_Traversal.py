class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, startvertex):

        queue = [startvertex]
        visited = {startvertex:True}



        while queue:
            currentvertex = queue.pop(0)
            print(currentvertex, end=' ')

            for neighbor in self.graph[currentvertex]:
                if neighbor not in visited:
                    visited[neighbor]=True
                    queue.append(neighbor)




#Example usage
g = Graph()
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','D')
g.add_edge('B','E')
g.add_edge('C','F')

print("dfs starting from vertex 'A:")
g.dfs('A')
print("\nbfs starting from vertex 'A:")
g.bfs('A')






