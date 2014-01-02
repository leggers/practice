#!/usr/bin/python
# Author: Lucas Eggers

# Implementation of a graph

class Graph:
    """Graph data structure"""
    def __init__(self, graphString = ''):
        self.vertices = []
        self.edges = []

    def add_vertex(self, name):
        vertex = Vertex(name)
        self.vertices.append(vertex)
        return vertex

    def connect_vertices(self, v1, v2):
        edge = Edge(v1, v2)
        self.edges.append(edge)
        return edge

    def disconnect_vertices(self, v1, v2):
        for edge in self.edges:
            if edge.connected_to(v1) and edge.connected_to(v2):
                edge.remove()
                return True
        return False


class Edge:
    """A graph edge"""
    def __init__(self, v1, v2):
        v1.edges.append(self)
        v2.edges.append(self)
        self.v1 = v1
        self.v2 = v2

    def other_end(self, v):
        if v == self.v1:
            return self.v2
        else:
            return self.v1

    def connected_to(self, vertex):
        return vertex == self.v1 or vertex == self.v2

    def remove(self):
        self.v1.remove_edge(self)
        self.v1 = None
        self.v2.remove_edge(self)
        self.v2 = None


class Vertex:
    """A graph vertex"""
    def __init__(self, name, weight = 1):
        self.name = name
        self.edges = []
        self.weight = weight

    def add_edge(self, edge):
        self.edges.append(edge)

    def remove_edge(self, edge):
        try:
            self.edges.remove(edge)
            return True
        except ValueError:
            return False