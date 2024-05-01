class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

        if v in self.graph:
            self.graph[v].append(u)
        else:
            self.graph[v] = [u]

    def printGraph(self):
        for vertex, neighbors in self.graph.items():
            print(f"Vertex {vertex}: ", end="")
            print(", ".join(str(neighbor) for neighbor in neighbors))

    def dfs(self, v, visited=None):
        if visited is None:
            visited = set()
        visited.add(v)
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            v = queue.pop(0)
            if v not in visited:
                print(v, end=' ')
                visited.add(v)
                queue.extend([neighbor for neighbor in self.graph[v] if neighbor not in visited])

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)


print("Graph representation:")
g.printGraph()

print("\nDFS traversal:")
g.dfs(0)

print("\nBFS traversal:")
g.bfs(0)
