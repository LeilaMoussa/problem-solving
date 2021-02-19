"""
Use a hashset $ and doubly linked list to implement an LRU cache.
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
        self.tail = None # Rear.

    def insert_at_head(self, new_elt: int):
        if not self.head:
            self.head = self.tail = Node(new_elt)
        else:
            new_node = Node(new_elt)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        
    def remove_node(self, val: int):
        walker = self.head
        while walker and walker.value != val:
            walker = walker.next
        if not walker:
            return
        walker.prev.next = walker.next
        if walker.next:
            walker.next.prev = walker.prev
        else:
            self.tail = self.tail.prev
        del walker

    def remove_last(self):
        if not self.head:
            return
        if self.head == self.tail:  # Need __eq__? Guess not.
            del self.head
            return
        last_val = self.tail.value
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        del temp
        return last_val

    def get_size(self):
        walker = self.head
        cnt = 0
        while walker:
            walker = walker.next
            cnt += 1
        return cnt

    def print_elements(self):
        walker = self.head
        while walker:
            print(walker.value, end=' ')
            walker = walker.next
        print('\n')

class LRU_cache:
    def __init__(self, capacity: int):
        self.elements = LinkedList()
        self.hash = defaultdict(int)
        # Should be a hash set: constant lookup set of unique elements.
        # I'll just give a random integer as a value
        self.capacity = capacity

    def lookup(self, elt: int):
        if elt not in self.hash and self.elements.get_size() == self.capacity:
            # It would definitely be better to have a size attribute here
            # but whatever.
            last_val = self.elements.remove_last()
            del self.hash[last_val]
        elif elt in self.hash:
            self.elements.remove_node(elt)
        self.elements.insert_at_head(elt)
        self.hash[elt] = 1  # Might want to look into a more elegant way of implementing hash.

    def display(self):
        print("Cache elements:")
        self.elements.print_elements()
        print("Hash set:")
        for k, v in self.hash.items():
            print(k, end=' ')
        print('\n')

if __name__ == '__main__':
    capacity = 3
    lookup_seq = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    lru = LRU_cache(capacity)
    for elt in lookup_seq:
        lru.lookup(elt)
    lru.display()
