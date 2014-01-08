#!usr/bin/python
# Author: Lucas Eggers

# A binary tree data structure

class BinaryTree(object):
    """A binary tree data structure"""
    def __init__(self):
        super(BinaryTree, self).__init__()
        self.root = None

    def is_empty(self):
        return self.root == None

    def insert(self, value, parent = None, child = None):
        if parent == None and not self.root == None:
            raise Exception("No parent specified for a non-root node")
        if not child.is_a_child_of(parent):
            raise Exception("Inserting between two non-connected nodes")

        new_node = TreeNode(value, parent)

        if self.root == None:
            self.root = new_node

        if child.is_left_child_of(parent):
            parent.left_child = new_node
            new_node.left_child = child
        elif child.is_right_child_of(parent):
            parent.right_child = new_node
            new_node.right_child = child



class TreeNode(object):
    """A node in a binary tree"""
    def __init__(self, value, parent, left_child = None, right_child = None):
        super(TreeNode, self).__init__()
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def is_a_child_of(self, node):
        return self.is_left_child_of(node) or self.is_right_child_of(node)

    def is_a_parent_of(self, node):
        return node == self.left_child or node == self.right_child

    def is_left_child_of(self, node):
        return node == self.left_child

    def is_right_child_of(self, node):
        return node == self.right_child

    def add_child(self, node):
        if self.left_child == None:
            self.left_child = node
        elif self.right_child == None:
            self.right_child = node
        else:
            raise Exception("Adding a child to a node with two children")