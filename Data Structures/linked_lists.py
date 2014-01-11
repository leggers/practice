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
        new_node = SinglyLinkedNode(value, self.first)
        self.first = new_node
        return new_node

    def insert_after(self, node, value):
        new_node = SinglyLinkedNode(value, node.next)
        node.next = new_node
        return new_node

    def remove_beginning(self):
        old_beginning = self.first
        self.first = old_beginning.next
        old_beginning.next = None
        return old_beginning.value

    def remove_after(self, node):
        to_remove = node.next
        node.next = to_remove.next
        to_remove.next = None
        return to_remove.value


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
        

class DoublyLinkedNode(object):
    """Doubly-linked list node"""
    def __init__(self, value, next = None, previous = None):
        super(DoublyLinkedNode, self).__init__()
        self.value = value
        self.next = next
        self.previous = previous
