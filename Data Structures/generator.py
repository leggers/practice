#!/usr/bin/python
# Author: Lucas Eggers

# Class for generating arbitrary data structures

from graph import *
import random

class Generator:
    """Class that generates various data structures."""

    def graph_nb(self, nodes, branching):
        """Generates a random undirected graph with a number of edges 
        per node. Does not allow nodes to connect to each other more 
        than once. Edges have default weight of one."""
        g = self.setup_graph(nodes)
        for vertex in g.vertices:
            connections = len(vertex.edges)
            for j in range(connections, branching):
                neighbor = random.choice( g.vertices )
                while neighbor == vertex or g.are_adjacent(vertex, neighbor):
                    neighbor = random.choice( g.vertices )
                g.connect_vertices(vertex, neighbor)
        return g

    def graph_nb_weighted(self, nodes, branching, min_weight, max_weight):
        """Creates a random graph with a number of edges per node.
        Does not allow nodes to connect to each other. Edges have
        integer weight between 1 and max_weight."""
        g = self.graph_nb(nodes, branching)
        for edge in g.edges:
            edge.weight = random.choice(range(min_weight, max_weight))
        return g

    def graph_nbd(self, nodes, branching):
        """Creates a directed graph with passed number of edges per node.
        For each edge, v1 denotes source vertex and v2 denotes destination.
        Edges have default weight of one."""
        g = self.setup_graph(nodes)
        curr = g.vertices[0]
        while not self.fully_connected(g, branching):
            connections = len(curr.edges)
            for i in range(connections, branching):
                neighbor = random.choice( g.vertices )
                while neighbor == curr or g.are_adjacent(curr, neighbor):
                    neighbor = random.choice( g.vertices )
                g.connect_vertices(curr, neighbor)
            curr = random.choice( g.neighbors_of(curr) )
        return g

    def graph_nbd_weighted(self, nodes, branching, min_weight, max_weight):
        """Generates a random directed graph with edge weights between the
        passed values."""
        g = self.graph_nbd(nodes, branching)
        for edge in g.edges:
            edge.weight = random.choice(range(min_weight, max_weight))
        return g

    def setup_graph(self, nodes):
        """Creates a graph with the passed number of nodes and no edges."""
        g = Graph()
        name_ord = ord('a') - 1
        for i in range(0, nodes):
            name_ord += 1
            g.add_vertex(chr(name_ord))
        return g

    def fully_connected(self, graph, branching):
        for vertex in graph.vertices:
            if len(vertex.edges) < 2:
                return False
        return True