#!/usr/bin/python
# Author: Lucas Eggers

# Class that implements the Bellman-Ford graph search algorithm.
# Useful for dealing with negative edge weights.

from generic_solver import *

class Bellman_Ford(GenericSolver):
    """Class that implements the Bellman-Ford graph search algorithm.
    Useful for dealing with negative edge weights."""
    def __init__(self, graph = None):
        super(Bellman_Ford, self).__init__(graph)

    def solve(self, initial, graph = None):
        graph = self.get_graph(graph)
        graph = self.setup(graph, initial)
        for i in range(0, len(graph.vertices)):
            for edge in graph.edges:
                v1 = self.get_v1(edge)
                v2 = edge.other_end(v1)
                distance_to_vertex = v1.distance + edge.weight
                if distance_to_vertex < v2.distance:
                    v2.distance = distance_to_vertex
                    v2.previous = v1

        for edge in graph.edges:
            v1 = self.get_v1(edge)
            v2 = edge.other_end(v1)
            distance_to_vertex = v1.distance + edge.weight
            if distance_to_vertex < v2.distance:
                raise Exception("Graph contains a negative-weight cycle")

    def setup(self, graph, initial):
        for vertex in graph.vertices:
            dist = float('inf')
            if vertex == initial:
                dist = 0
            vertex.distance = dist
            vertex.previous = None
        return graph

    def get_v1(self, edge):
        v1 = edge.v1
        # starting node has no previous and distance is 0
        if v1.previous == None and v1.distance == 0:
            return v1
        # some path exists to this node
        elif v1.previous:
            return v1
        # otherwise, return the other one
        else:
            return edge.v2