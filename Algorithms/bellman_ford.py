#!/usr/bin/python
# Author: Lucas Eggers

# Class that implements the Bellman-Ford graph search algorithm.
# Useful for dealing with negative edge weights.

from generic_solver import *

class Bellman_Ford(GenericSolver):
    """Class that implements the Bellman-Ford graph search algorithm.
    Useful for dealing with negative edge weights."""
    def __init__(self, graph):
        super(Bellman_Ford, self).__init__(graph)