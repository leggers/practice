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

    def remove(self, node):
        parent = node.parent
        node.parent = None

        if node.is_left_child_of(parent):
            parent.left_child = None

            if node.left_child:
                parent.left_child = node.left_child
                node.left_child.parent = parent
                # if node we're removing has two chilren
                if node.right_child:
                    node.left_child.right_child = node.right_child
                    node.right_child.parent = node.left_child

            elif node.right_child:
                parent.left_child = node.right_child
                node.right_child.parent = parent

        elif node.is_right_child_of(parent):
            parent.right_child = None

            if node.right_child:
                parent.right_child = node.right_child
                node.right_child.parent = parent
                if node.left_child:
                    node.right_child.left_child = node.left_child
                    node.left_child.parent = node.left_child

            elif node.left_child:
                parent.right_child = node.left_child
                node.left_child.parent = parent

        else:
            raise Exception("Node is not a child of its supposed parent. Uh oh")




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
        return node.left_child == self

    def is_right_child_of(self, node):
        return node.right_child == self

    def add_child(self, node):
        if self.left_child == None:
            self.left_child = node
        elif self.right_child == None:
            self.right_child = node
        else:
            raise Exception("Adding a child to a node with two children")

    def is_leaf(self):
        return self.left_child == None and self.right_child == None

    def number_of_children(self):
        number = 0
        if self.left_child:
            number += 1
        if self.right_child:
            number += 1
        return number