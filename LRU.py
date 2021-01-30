from collections import defaultdict

# Doubly LL.

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

class LRU_cache:
    def __init__(self):
        self.elements = LinkedList()
        self.records = defaultdict(int)
        self.timestamp = 0

    def lookup(self, elt):
        self.timestamp += 1
        
