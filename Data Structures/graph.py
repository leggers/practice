#!/usr/bin/python
# Author: Lucas Eggers

# Inicidence list implementation of a graph data structure.

class Graph:
    """Graph data structure. The graph is structured as an indidence list."""
    def __init__(self, graphString = ''):
        self.vertices = []
        self.edges = []

    def to_string(self):
        for vertex in self.vertices:
            to_print = str(vertex.value) + ': '
            for neighbor in self.neighbors_of(vertex):
                to_print += str( self.get_edge_weight(vertex, neighbor) ) + ' to '
                to_print += str(neighbor.value) + ', '
            print to_print

    def add_vertex(self, value):
        """Adds a vertex with a given value"""
        vertex = Vertex(value)
        self.vertices.append(vertex)
        return vertex

    def connect_vertices(self, v1, v2, weight = 1):
        """Adds an edge between two passed vertices. Can assign a weight to
        the edge as an optional parameter."""
        edge = Edge(v1, v2, weight)
        self.edges.append(edge)
        return edge

    def disconnect_vertices(self, v1, v2):
        """Removes the edge connecting the vertices. Returns the edge's
        weight (default of 1)."""
        edge = self.get_edge_between(v1, v2)
        if edge:
            weight = edge.weight
            edge.remove()
            return weight
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

    def get_edge_weight(self, v1, v2):
        return self.get_edge_between(v1, v2).weight

    def set_edge_weight(self, v1, v2, weight):
        """Set the weight of the edge between two vertices."""
        self.get_edge_between(v1, v2).weight = weight

    def get_edge_between(self, v1, v2):
        """Get the edge connecting two vertices."""
        for edge in self.edges:
            if edge.connected_to(v1) and edge.connected_to(v2):
                return edge
        raise Exception("No edge exists between passed nodes.")


class Edge:
    """A graph edge. Stores its incident vertices and possibly a weight."""
    def __init__(self, v1, v2, weight):
        v1.edges.append(self)
        v2.edges.append(self)
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def other_end(self, v):
        """Gets node on the other end of the """
        if v == self.v1:
            return self.v2
        elif v == self.v2:
            return self.v1
        else:
            raise Exception("Edge not connected to passed node.")

    def connected_to(self, vertex):
        """Returns whether or not passed vertex is connected to edge."""
        return vertex == self.v1 or vertex == self.v2

    def remove(self):
        """Remove edge from the graph. Removes reference to edge from
        connected vertices and removes references to vertices from self."""
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
        """Adds edge to vertex's edge list."""
        self.edges.append(edge)

    def remove_edge(self, edge):
        """Removes edge from vertex's edge list."""
        try:
            self.edges.remove(edge)
        except ValueError:
            raise Exception("Vertex not connected to passed edge.")