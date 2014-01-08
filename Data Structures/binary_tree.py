#!usr/bin/python
# Author: Lucas Eggers

# A binary tree data structure

class BinaryTree(object):
    """A binary tree data structure. A naive implementation.
    Not a balanced tree or even a search tree. Just an arbitrary tree."""
    def __init__(self):
        super(BinaryTree, self).__init__()
        self.root = None

    def is_empty(self):
        """Returns whether or not the tree is empty"""
        return self.root == None

    def insert(self, value, parent = None, child = None):
        """Inserts a new node into the tree. Can be inserted between two nodes
        by specifying the parent and child nodes. Can be added as leaf by 
        only specifying parent (if that parent does not already have two children!"""
        new_node = TreeNode(value, parent)

        # adding or replacing a root node
        if self.is_empty():
            self.root = new_node
        elif child == self.root:
            self.root = new_node
            new_node.add_child(child)

        if parent:
            if child:
                if not child.is_a_child_of(parent):
                    raise Exception("Inserting between two non-connected nodes")
                elif child.is_left_child_of(parent):
                    parent.left_child = new_node
                    new_node.left_child = child
                elif child.is_right_child_of(parent):
                    parent.right_child = new_node
                    new_node.right_child = child
                child.parent = new_node
            else:
                parent.add_child(new_node)
        else:
            if not new_node == self.root:
                raise Exception("Cannot add a non-root node without a parent")

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
            node.parent = self
        elif self.right_child == None:
            self.right_child = node
            node.parent = self
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