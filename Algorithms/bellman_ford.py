#!/usr/bin/python
# Author: Lucas Eggers

# Class that implements the Bellman-Ford graph search algorithm.
# Useful for dealing with negative edge weights.

from generic_solver import *

class Bellman_Ford(GenericSolver):
    """Class that implements the Bellman-Ford graph search algorithm.
    Useful for dealing with negative edge weights."""
    def __init__(self, graph):
        super(Bellman_Ford, self).__init__(graph)

    def solve(self, initial, graph):
        graph = self.setup(graph, initial)
        for i in range(0, len(graph.vertices)):
            for edge in graph.edges:
                distance_to_vertex = edge.v1.distance + edge.weight
                if distance_to_vertex < edge.v2.distance:
                    edge.v2.distance = distance_to_vertex
                    edge.v2.previous = edge.v1

        for edge in graph.edges:
            distance_to_vertex = edge.v1.distance + edge.weight
            if distance_to_vertex < edge.v2.distance:
                railse "Graph contains a negative-weight cycle"

    def setup(self, graph, initial):
        for vertex in graph.vertices:
            dist = float('inf')
            if vertex == initial:
                dist = 0
            vertex.distance = dist
            vertex.previous = None
        return graph