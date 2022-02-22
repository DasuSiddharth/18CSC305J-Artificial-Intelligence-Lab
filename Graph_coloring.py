class Graph:
      def __init__ (self, edges, N):
        self.adj = [[] for _ in range(N)] 
        for (src, dest) in edges:
          self.adj[src].append(dest) 
          self.adj[dest].append(src)

def colorGraph(graph):
    result = {}
    for u in range(N):
      assigned = set([result.get(i) for i in graph.adj[u] if i in result]) 
      color = 1
      for c in assigned:
        if color != c:
            break
        color = color + 1 
      result[u] = color
    for v in range(N):
        print("color assigned to vertex", v, "is",colors[result[v]])
    print("\n")
    for v in range(N):
        print("color assigned to Edge", v, "is",colors[result[v]+3])

if __name__ == '__main__':
    colors= ["", "YELLOW", "RED", "BLUE", "ORANGE", "GREEN", "PINK", "BLACK", "BROWN", "WHITE", "PURPLE", "VIOLET"]
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]
    N = 5
    graph = Graph(edges, N) 
    colorGraph(graph)
