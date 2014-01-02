#!/usr/bin/python
# Author: Lucas Eggers

# Implementation of a graph

class Graph:
    """Graph data structure. The graph is structured as an indidence list."""
    def __init__(self, graphString = ''):
        self.vertices = []
        self.edges = []

    def add_vertex(self, value):
        """Adds a vertex with a given value"""
        vertex = Vertex(value)
        self.vertices.append(vertex)
        return vertex

    def connect_vertices(self, v1, v2, value = 1):
        """Adds an edge between two passed vertices. Can assign a value to
        the edge as an optional parameter."""
        edge = Edge(v1, v2, value)
        self.edges.append(edge)
        return edge

    def disconnect_vertices(self, v1, v2):
        """Removes the edge connecting the vertices. Returns the edge's
        value if one was assigned."""
        edge = self.get_edge_between(v1, v2)
        if edge:
            value = edge.value
            if value == None:
                value = True
            edge.remove()
            return value
        return False

    def neighbors_of(self, vertex):
        """Get all neighbors of a vertex."""
        neighbors = []
        for edge in vertex.edges:
            neighbors.append( edge.other_end(vertex) )
        return neighbors

    def are_adjacent(self, v1, v2):
        """Boolean whether or not two vertices have an edge between them."""
        for edge in v1.edges:
            if edge.connected_to(v2):
                return True
        return False

    def get_edge_value(self, v1, v2):
        edge = self.get_edge_between(v1, v2)
        if edge:
            return edge.value
        raise "No edge exists between passed nodes!"

    def set_edge_value(self, v1, v2, value):
        """Set the value of the edge between two vertices."""
        edge = self.get_edge_between(v1, v2)
        if edge:
            edge.value = value
        else:
            raise "No edge exists between passed nodes!"

    def get_edge_between(self, v1, v2):
        """Set the value of the edge between two vertices."""
        for edge in self.edges:
            if edge.connected_to(v1) and edge.connected_to(v2):
                return edge
        return None


class Edge:
    """A graph edge"""
    def __init__(self, v1, v2, value):
        v1.edges.append(self)
        v2.edges.append(self)
        self.v1 = v1
        self.v2 = v2
        self.value = value

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
    def __init__(self, value):
        self.value = value
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def remove_edge(self, edge):
        try:
            self.edges.remove(edge)
            return True
        except ValueError:
            return False