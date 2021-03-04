""" A red black tree is a special case of a binary search tree (BST)
that is self-balancing to always guarantee O(logn) operations.
"""

class Node:
    def __init__(self, color: int, value: int):
        self.color = color  # Let's say 0 is black and 1 is red.
        self.value = value
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self): # value $$$$$$$$$
        self.root = Node(0)

    def search(self, root: Node, value: int) -> Node:
        # Normal BST search.
        if root == None or root.value == value:  # Short circuit expression.
            return root
        if root.value > value:
            return self.search(root.left, value)
        return self.search(root.right, value)
        
    def insert(self, value: int) -> bool:
        pass

    def delete(self, value: int) -> bool:
        pass

    def display(self) -> None:
        pass

# Can I interleave operations to test?
tree = RedBlackTree()
