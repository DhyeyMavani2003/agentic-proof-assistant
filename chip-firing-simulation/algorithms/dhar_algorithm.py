class DharAlgorithm:
    def __init__(self, graph, configuration, q):
        self.graph = graph
        self.configuration = {v: configuration[v] for v in graph if v != q}
        self.q = q
        self.unburnt_vertices = set(self.configuration.keys())

    def outdegree_S(self, vertex, S):
        return sum(self.graph[vertex][neighbor] for neighbor in self.graph[vertex] if neighbor in S)

    def run(self):
        S = set(self.unburnt_vertices)
        while S:
            found_vertex = False
            for v in list(S):
                if self.configuration[v] < self.outdegree_S(v, S):
                    S.remove(v)
                    found_vertex = True
                    break
            if not found_vertex:
                return S
        return set()
