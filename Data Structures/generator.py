#!/usr/bin/python
# Author: Lucas Eggers

# Class for generating arbitrary data structures

from graph import *
import random

class Generator:
    """Class that generates various data structures."""

    def graph_nb(self, nodes, branching):
        """Generates a random graph with a number of edges per node.
        Does not allow nodes to connect to each other."""
        g = Graph()
        for i in range(0, nodes):
            g.add_vertex(i)
        for vertex in g.vertices:
            connections = len(vertex.edges)
            for j in range(connections, branching):
                neighbor = random.choice( g.vertices )
                while neighbor == vertex or g.are_adjacent(vertex, neighbor):
                    neighbor = random.choice( g.vertices )
                g.connect_vertices(vertex, neighbor)
        return g