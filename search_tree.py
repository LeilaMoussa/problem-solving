# what's an object oriented way to pick strategy?

# remember, in general, the fringe is the set of distinct paths found so far, not of nodes

def usc_strategy():
    # fringe is a priority queue
    pass

def dfs_strategy():
    # fringe is a LIFO stack
    pass

def bfs_strategy():
    # fringe is fifo queue
    pass

def build_tree(problem, strategy):
    # Return path or None
    pass

# define problem: start, end, states, successor
# pick strategy
