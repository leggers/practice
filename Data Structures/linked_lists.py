#!usr/bin/python
# Author: Lucas Eggers

# A linked list data structure

class SinglyLinkedList(object):
    """Singly linked list data structure"""
    def __init__(self):
        super(SinglyLinkedList, self).__init__()
        self.first = None

class SinglyLinkedNode(object):
    """Singly-linked list node"""
    def __init__(self, value, next = None):
        super(SinglyLinkedNode, self).__init__()
        self.value = value
        self.next = next



class DoublyLinkedList(object):
    """Doubly linked list data structure"""
    def __init__(self):
        super(DoublyLinkedList, self).__init__()
        self.first = None
        

class DoublyLinkedNode(object):
    """Doubly-linked list node"""
    def __init__(self, value, next = None, previous = None):
        super(DoublyLinkedNode, self).__init__()
        self.value = value
        self.next = next
        self.previous = previous
