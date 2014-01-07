#!/usr/bin/python
# Author: Lucas Eggers

# Class that implements the Bellman-Ford graph search algorithm.
# Useful for dealing with negative edge weights.

class Bellman_Ford:
    """Class that implements the Bellman-Ford graph search algorithm.
    Useful for dealing with negative edge weights."""
    def __init__(self, graph):
        self.graph = graph
