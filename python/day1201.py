"""
Daily Coding Problem: #1201
Date: 4-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
"""
Problem:
Write an algorithm that computes the reversal of a directed graph. 
For example, if a graph consists of A -> B -> C, it should become A <- B <- C.
"""
"""
Solution:
    The solution of this problem varies based on the input.
    As we can represent (Directed) Graph in three ways, so we have three solutions
        => edge list: just reverse each pair of edge
        => adjacency matrix: simply transpose this matrix
        => adjacency list: We are presenting this solution below
"""




from collections import defaultdict
class Graph:
    def __init__(self):
        self.adj_list = defaultdict(defaultdict)

    def add_edge(self, u, v, weight=1):
        # Here I'm assuming that each vertices pair can have at-max one edge only
        # Else we have to maintain a list of weight instead of just one int
        self.adj_list[u][v] = weight

    def delete_edge(self, u, v):
        del self.adj_list[u][v]

    def transpose(self):
        graph = Graph()
        for u in self.adj_list.keys():
            for v in self.adj_list[u].keys():
                graph.add_edge(v, u)
        return graph

    def has_edge(self, u, v):
        return self.adj_list[u].get(v) != None

    def edge_count(self):
        edge_count = 0
        for u in self.adj_list.keys():
            edge_count += len(self.adj_list[u].keys())
        return edge_count


def test():
    graph = Graph()
    graph.add_edge('a', 'b')
    graph.add_edge('b', 'c')
    graph.add_edge('b', 'd')
    graph.add_edge('c', 'd')

    transpose_graph = graph.transpose()

    assert transpose_graph.edge_count() == 4, "There should be only 4 edges"
    assert transpose_graph.has_edge(
        'b', 'a') == True, "There should be an edge between b to a"
    assert transpose_graph.has_edge(
        'a', 'b') == False, "There should not be an edge between a to b"
    assert transpose_graph.has_edge(
        'c', 'b') == True, "There should be an edge between c to b"
    assert transpose_graph.has_edge(
        'b', 'c') == False, "There should not be an edge between b to c"
    assert transpose_graph.has_edge(
        'd', 'b') == True, "There should be an edge between d to b"
    assert transpose_graph.has_edge(
        'b', 'd') == False, "There should not be an edge between b to d"
    assert transpose_graph.has_edge(
        'd', 'c') == True, "There should be an edge between d to c"
    assert transpose_graph.has_edge(
        'c', 'd') == False, "There should not be an edge between c to d"


if __name__ == "__main__":
    test()
