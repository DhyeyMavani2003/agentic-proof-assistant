from collections import defaultdict

class GreedyAlgorithm:
    def __init__(self, graph, divisor):
        """
        Initialize the greedy algorithm for the dollar game.
        
        :param graph: A dictionary representing the adjacency list of the graph.
        :param divisor: A dictionary representing the wealth at each vertex.
        """
        self.graph = graph
        self.divisor = divisor
        self.marked_vertices = set()
        self.firing_script = defaultdict(int)

    def is_effective(self):
        """
        Check if all vertices have non-negative wealth.
        
        :return: True if effective, otherwise False.
        """
        return all(wealth >= 0 for wealth in self.divisor.values())

    def borrowing_move(self, vertex):
        """
        Perform a borrowing move at the specified vertex.
        
        :param vertex: The vertex at which to perform the borrowing move.
        """
        for neighbor, edge_count in self.graph[vertex].items():
            total_borrowed = edge_count
            self.divisor[neighbor] -= total_borrowed
            self.divisor[vertex] += total_borrowed
        self.firing_script[vertex] += 1

    def play(self):
        """
        Execute the greedy algorithm to determine winnability.
        
        :return: Tuple (True, firing_script) if the game is winnable; otherwise (False, None).
        """
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