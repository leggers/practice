#!/usr/bin/python
# Author: Lucas Eggers

# Class that implements Dijkstra's graph search algorithm

class Dijkstra():
    """Class that implements Dijstra's graph serach algorithm"""
    def __init__(self, graph = None):
        self.graph = graph

    def solve(self, initial, graph = None):
        """Returns a graph with previous pointers and distances
        attached to each node that point back to the start node."""
        graph = self.get_graph(graph)
        nodes = self.setup(graph, initial)
        while len(nodes) > 0:
            current = self.get_closest_node(nodes)
            nodes.remove(current)
            if not current:
                raise "Disjoint graph passed"
            for neighbor in graph.neighbors_of(current):
                distance = current.distance + graph.get_edge_weight(current, neighbor)
                if distance < neighbor.distance:
                    neighbor.distance = distance
                    neighbor.previous = current
        initial.previous = None
        return graph


    def path_to(self, node):
        """Prints the solutions as a string."""
        path = [node]
        while node.previous:
            path.append(node.previous)
            node = node.previous
        return path[::-1]

    def get_graph(self, graph):
        """Returns the graph to analyse"""
        if not graph:
            graph = self.graph
            if not graph:
                raise "No graph provided in constructor or method call"
        return graph

    def setup(self, graph, initial):
        """Sets up the mapping from nodes to distances"""
        for vertex in graph.vertices:
            dist = float('inf')
            if vertex == initial:
                dist = 0
            vertex.distance = dist
        return set(graph.vertices)

    def get_closest_node(self, nodes):
        dist = float('inf')
        for node in nodes:
            if node.distance < dist:
                closest = node
        return closest