#!/usr/bin/python
# Author: Lucas Eggers

# Inicidence list implementation of a graph data structure.

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
        return self.get_edge_between(v1, v2).value

    def set_edge_value(self, v1, v2, value):
        """Set the value of the edge between two vertices."""
        self.get_edge_between(v1, v2).value = value

    def get_edge_between(self, v1, v2):
        """Set the value of the edge between two vertices."""
        for edge in self.edges:
            if edge.connected_to(v1) and edge.connected_to(v2):
                return edge
        raise "No edge exists between passed nodes."


class Edge:
    """A graph edge. Stores its incident vertices and possibly a value."""
    def __init__(self, v1, v2, value):
        v1.edges.append(self)
        v2.edges.append(self)
        self.v1 = v1
        self.v2 = v2
        self.value = value

    def other_end(self, v):
        """Gets node on the other end of the """
        if v == self.v1:
            return self.v2
        elif v == self.v2:
            return self.v1
        else:
            raise "Edge not connected to passed node."

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
            raise "Vertex not connected to passed edge."