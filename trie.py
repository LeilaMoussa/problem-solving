"""
To do:
- Finish Trie with list implementation
- Do TrieNode2
- Do Trie with dictionary implementation
- Test a little
- Submit a modified version to LeetCode
- Discuss performance and tradeoffs
- All time & space complexities
"""

alphabet = 26
mode = 1  # To switch between node implementations.

class TrieNode1:
    # Implemented as a list of references.
    
    def __init__(self):
        self.children = [None]*alphabet
        # Each possible following character is represented as a cell in this array. A node can have 0 to 26 children.
        # Cell is None if the character does not exist in the following level.
        # Cell contains reference to another TrieNode if it's there.
        # ==> This list expresses the OUTGOING links.
        self.is_end = False
        # Is the current node the last character of a word?

    def __get_index(self, char: str) -> int: # Private utility function. Does it need self?
        return ord(char) - ord('a')
        
    def has_child(self, char: str) -> bool:
        # Does the current node point to this character?
        # We need to know this for traversal.
        return self.children[self.__get_index(char)] != None

    def add_child(self, char: str, new_node: TrieNode1) -> None:
        self.children[self.__get_index(char)] = new_node

    def get_child(self, char: str) -> TrieNode:
        return self.children[self.__get_index(char)]  # Could return None.
        

class TrieNode2:
    # Implemented as a dictionary of references.
    # Added a count attribute that expresses how many words contain this node (like how the words overlap),
    #   both for variety and for deleting

    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0

    def add_child(self, char: str) -> None:
        pass

    def has_child(self, char: str) -> bool:
        pass

    def get_child(self, char: str) -> TrieNode2:
        pass

class Trie:
    def __init__(self):
        if mode == 1:
            self.root = TrieNode1()
            
        else:
            self.root = TrieNode2()

    def __search_prefix(self, word: str):
        # This function returns the last node if the prefix is found, and None otherwise.
        # I am abstracting this method away because it is used both in search() and starts_with()
        current = self.root
        for i, char in enumerate(word):
            if not current.contains_child(char):
                return None
            current = current.get_child(char)
        return current

    def search(self, word: str) -> bool:
        if mode == 1:
            last_node = self.__search_prefix(word)
            # At this point, we know all characters exist, but we don't know if the word is there or
            #   if it's just a prefix for another word.
            # So check whether the last node is the end.
            return current != None and current.is_end
                    
        else:
            pass

    def insert(self, word: str) -> None:
        # While a prefix already exists, just traverse.
        # Once the prefix no longer exists, create new nodes.
        if mode == 1:
            current = self.root  # Remember, this is a node.
            for char in word:  # O(m)
                if not current.has_child(char):
                    current.add_child(char, TrieNode1())
                current = current.get_child(char)
            current.is_end = True  # hmm.
            
        else:
            pass

    def starts_with(self, prefix: str) -> bool:
        # Returns if there is any word in the trie that starts with the given prefix.
        if mode == 1:
            # Almost the same logic as search; one difference: no need to check for is_end at the end.
            return self.__search_prefix(prefix) != None
        else:
            pass
                
    def delete(self, word: str, current=self.root, depth=0) -> bool: # Not sure if this signature will be okay.
        # I am only implementing this for the dictionary implementation because that is where I chose to include a count.
        # A count is necessary for overlapping words.
        if mode == 2:
            # Delete recursively, bottom up.

            # Traverse till the bottom of the word, then bubble up deleting (or decrementing counts).
            # If at the bottom, remove the `is_end` marker (check first if it is the end of a word -- otherwise, the word doesn't exist
            #   and it doesn't make sense to delete it.)
            # To delete: look at count: is it 0? Then delete the node. Otherwise, just decrement the counter.

            # If we're not at the bottom yet, make a recursive call.
            pass

    def isEmpty(self) -> bool:
        if mode == 1:
            for child in self.root.children:
                if child != None:
                    return False
            return True
        else:
            pass
            

# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
