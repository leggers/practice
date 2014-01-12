#!usr/bin/python
# Author: Lucas Eggers

# A linked list data structure

class AbstractList(object):
    """Class that implements shared list methods"""
    def __init__(self):
        super(AbstractList, self).__init__()
        self.first = None


class SinglyLinkedList(AbstractList):
    """Singly linked list data structure"""
    def __init__(self):
        super(SinglyLinkedList, self).__init__()

    def insert_at_beginning(self, value):
        """Inserts new node at beginning of list"""
        new_node = SinglyLinkedNode(value, self.first)
        self.first = new_node
        return new_node

    def insert_after(self, node, value):
        """Inserts node after passed node"""
        new_node = SinglyLinkedNode(value, node.next)
        node.next = new_node
        return new_node

    def remove_beginning(self):
        """Removes first node of list"""
        old_beginning = self.first
        self.first = old_beginning.next
        old_beginning.next = None
        return old_beginning.value

    def remove_after(self, node):
        """Removes node after passed node"""
        to_remove = node.next
        node.next = to_remove.next
        to_remove.next = None
        return to_remove.value

    def to_string(self):
        """Returns string representation of list"""
        node = self.first
        to_return = "Empty List"
        if node:
            to_return = str(node.value)
            while node.next:
                to_return += " -> "
                node = node.next
                to_return += str(node.value)
        return to_return


class SinglyLinkedNode(object):
    """Singly-linked list node"""
    def __init__(self, value, next = None):
        super(SinglyLinkedNode, self).__init__()
        self.value = value
        self.next = next



class DoublyLinkedList(AbstractList):
    """Doubly linked list data structure"""
    def __init__(self):
        super(DoublyLinkedList, self).__init__()
        self.last = None

    def insert_at_beginning(self, value):
        """Inserts node at beginning of list"""
        if self.first == None:
            new_node = DoublyLinkedNode(value, self.first)
            self.first = new_node
            self.last = new_node
        else:
            new_node = self.insert_before(self.first, value)
        return new_node

    def insert_at_end(self, value):
        """Inserts node at end of list"""
        if self.last == None:
            new_node = self.insert_at_beginning(value)
        else:
            new_node = self.insert_after(self.last, value)
        return new_node

    def insert_after(self, node, value):
        """Inserts node after passed node"""
        new_node = DoublyLinkedNode(value, node.next, node)
        if node.next == None:
            self.last = new_node
        else:
            node.next.previous = new_node
        node.next = new_node
        return new_node

    def insert_before(self, node, value):
        """Inserts node before passed node"""
        new_node = DoublyLinkedNode(value, node, node.previous)
        if node.previous == None:
            self.first = new_node
        else:
            node.previous.next = new_node
        node.previous = new_node
        return new_node

    def remove(self, node):
        """Removes passed node"""
        # first node of list
        if node.previous == None:
            self.first = node.next
        else:
            node.previous.next = node.next

        # last node of list
        if node.next == None:
            self.last = node.previous
        else:
            node.next.previous = node.previous

        return node.value

    def to_string(self):
        """Returns string representation of list"""
        node = self.first
        to_return = "Empty List"
        if node:
            to_return = str(node.previous) + " <-> " + str(node.value)
            while node.next:
                to_return += " <-> "
                node = node.next
                to_return += str(node.value)
            to_return += " <-> " + str(node.next)
        return to_return

class DoublyLinkedNode(object):
    """Doubly-linked list node"""
    def __init__(self, value, next = None, previous = None):
        super(DoublyLinkedNode, self).__init__()
        self.value = value
        self.next = next
        self.previous = previous
