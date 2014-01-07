#!/usr/bin/python
# Author: Lucas Eggers

# A superclass of graph solvers to implement shared functionality

class GenericSolver(object):
    """Implements generic graph solving methods and some helpers"""
    def __init__(self, graph):
        super(GenericSolver, self).__init__()
        self.graph = graph

    def path_to(self, node):
        """Prints the solutions as a string."""
        path = [node]
        while node.previous:
            path.append(node.previous)
            node = node.previous
        return path[::-1]

    def get_graph(self, graph):
        """Returns the graph to analyse"""
        if not graph:
            graph = self.graph
            if not graph:
                raise Exception("No graph provided in constructor or method call")
        return graph