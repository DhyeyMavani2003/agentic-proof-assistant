from collections import defaultdict

class DollarGame:
    def __init__(self, graph, divisor):
        self.graph = graph
        self.divisor = divisor
        self.marked_vertices = set()
        self.firing_script = defaultdict(int)

    def is_effective(self):
        return all(wealth >= 0 for wealth in self.divisor.values())

    def borrowing_move(self, vertex):
        for neighbor, edge_count in self.graph[vertex].items():
            total_borrowed = edge_count
            self.divisor[neighbor] -= total_borrowed
            self.divisor[vertex] += total_borrowed
        self.firing_script[vertex] += 1

    def play_game(self):
        while not self.is_effective():
            in_debt_vertex = next((v for v in self.divisor if self.divisor[v] < 0), None)
            if in_debt_vertex is None:
                return True, self.firing_script

            self.borrowing_move(in_debt_vertex)
            
            if in_debt_vertex not in self.marked_vertices:
                self.marked_vertices.add(in_debt_vertex)
            else:
                if self.marked_vertices == set(self.graph.keys()):
                    return False, None
        return True, self.firing_script

    def laplacian_matrix(self):
        laplacian = defaultdict(lambda: defaultdict(int))
        for v in self.graph:
            degree = sum(self.graph[v].values())
            laplacian[v][v] = degree
            for w, edge_count in self.graph[v].items():
                laplacian[v][w] -= edge_count
        return laplacian

    def apply_laplacian(self, firing_script):
        laplacian = self.laplacian_matrix()
        resulting_divisor = defaultdict(int, self.divisor)
        for v in self.graph:
            for w in self.graph:
                resulting_divisor[v] -= laplacian[v][w] * firing_script[w]
        return resulting_divisor