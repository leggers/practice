#!/usr/bin/python
# Author: Lucas Eggers

# Implementation of a graph

class Graph:
    """Graph data structure"""
    def __init__(self, graphString):
        self.vertices = []
        self.edges = []

class Edge:
    """A graph edge"""
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

class Vertex:
    """A graph vertex"""
    def __init__(self, name):
        self.name = name