#!/usr/bin/python
# Author: Lucas Eggers

# Class for generating arbitrary data structures

from graph import *
import random

class Generator:
    """Class that generates various data structures."""

    def graph_nb(self, nodes, branching):
        """Generates a random graph with a number of edges per node.
        Does not allow nodes to connect to each other. Edges have
        default weight of one."""
        g = Graph()
        name_ord = ord('a') - 1
        for i in range(0, nodes):
            name_ord += 1
            g.add_vertex(chr(name_ord))
        for vertex in g.vertices:
            connections = len(vertex.edges)
            for j in range(connections, branching):
                neighbor = random.choice( g.vertices )
                while neighbor == vertex or g.are_adjacent(vertex, neighbor):
                    neighbor = random.choice( g.vertices )
                g.connect_vertices(vertex, neighbor)
        return g

    def graph_nb_weighted(self, nodes, branching, max_weight):
        """Creates a random graph with a number of edges per node.
        Does not allow nodes to connect to each other. Edges have
        integer weight between 1 and max_weight."""
        g = self.graph_nb(nodes, branching)
        for edge in g.edges:
            edge.weight = random.choice(range(1, max_weight))
        return g