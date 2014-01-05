#!/usr/bin/python
# Author: Lucas Eggers

# Class that implements Dijkstra's graph search algorithm

class Dijkstra():
    """Class that implements Dijstra's graph serach algorithm"""
    def __init__(self, graph = None):
        self.graph = graph

    def solve(self, initial, graph = None):
        """Returns a map from destination vertex to shortest path
        to that vertex, represented as an array of vertex, edge,
        vertex, edge, vertex, etc."""
        if not graph:
            graph = self.graph
            if not graph:
                raise "No graph provided in constructor or method call"
        print graph.to_string()

    def solution_string(self):
        """Prints the solutions as a string."""
        pass