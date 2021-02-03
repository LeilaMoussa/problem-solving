"""
Use a hashmap and doubly linked list to implement an LRU cache.
Hoping to do this very soon...
"""

from collections import defaultdict

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, new_elt):
        new_node = Node(new_elt)
        self.head.prev = new_node
        # ...
        
    def remove_node(self, val):
        pass

    def search(self, val):
        pass

class LRU_cache:
    def __init__(self):
        self.elements = LinkedList()
        self.records = defaultdict(int)
        self.timestamp = 0

    def lookup(self, elt):
        self.timestamp += 1
        # ...
        
