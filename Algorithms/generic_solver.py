#!/usr/bin/python
# Author: Lucas Eggers

# A superclass of graph solvers to implement shared functionality

class GenericSolver(object):
    """Implements generic graph solving methods and some helpers"""
    def __init__(self, graph):
        super(GenericSolver, self).__init__()
        self.graph = graph

