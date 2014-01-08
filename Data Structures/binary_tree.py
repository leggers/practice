#!usr/bin/python
# Author: Lucas Eggers

# A binary tree data structure

class BinaryTree(object):
    """A binary tree data structure"""
    def __init__(self):
        super(BinaryTree, self).__init__()

class TreeNode(object):
    """A node in a binary tree"""
    def __init__(self, value, parent, child = None):
        super(TreeNode, self).__init__()
        self.value = value
        self.parent = parent
        self.child = child