""" A red black tree is a special case of a binary search tree (BST)
that is self-balancing to always guarantee O(logn) operations.
"""

class Node:
    def __init__(self, color: str, value: int):
        self.color = color  # B or R
        self.value = value
        self.left = None
        self.right = None
        self.parent = None  # Important for being able to go back

class RedBlackTree:
    def __init__(self, color: str, value: int):
        self.root = Node(color, value)

    def search(self, root: Node, value: int) -> Node:
        # Normal BST search.
        if root == None or root.value == value:  # Short circuit expression.
            return root
        if root.value > value:
            return self.search(root.left, value)
        return self.search(root.right, value)

    def rotate_left(node: Node) -> Node:
        x = node.right
        y = x.left
        # Re-arranging references
        x.left = node
        node.right = y
        node.parent = x
        if y:
            # I need to better understand this line.
            y.parent = node
        return x  # This is the root now.

    def rotate_right(node: Node) -> Node:
        # Similar logic, but I need to digest it still.
        x = node.left
        y = x.right
        x.right = node
        node.left = y
        node.parent = x
        if y:
            y.parent = node
        return x

    # Let's see if it's okay to define class attributes here
    # Flags to determine which rotation to use
    # I need to better understand why these flags are set to True in the red-red case...
    ll = rr = rl = lr = False
    def insert_inner(self, root: Node, value: int) -> Node:
        c = False  # red-red conflict
        
        # First, insert like in regular BST
        if value > root.value:
            self.insert_inner(root.right, value)
            # Setting the parent -- I need to think more about why this is done here
            root.right.parent = root
            # In the following, I am deviating a bit from the example code to see what happens
            if root.color == 'R' and root.right.color == 'R':
                c = True
        else:
            self.insert_inner(root.left, value)
            self.left.parent = root
            if root.color == 'R' and root.left.color == 'R':
                c = True
                
        # Then rotate and recolor
        # This may not be the correct way to reference these attributes.
        if ll:
            root = rotate_left(root)
            root.color = 'B'
            root.left.color = 'R'
            ll = False
        elif rr:
            root = rotate_left(root)
            root.color = 'B'
            root.right.color = 'R'
            rr = False
        elif rl:
            pass
        elif lr:
            pass

        if c:
            pass
        
    def insert(self, value: int) -> bool:
        if self.root == None:
            self.root = Node('B', value)
        else:
            self.insert_inner(self.root, value)

    def delete(self, value: int) -> bool:
        pass

    def display(self) -> None:
        pass

# Can I interleave operations to test?
tree = RedBlackTree()
