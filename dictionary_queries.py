from collections import defaultdict
from functools import reduce
import re

def regex(words: list, queries: list):
    # Time & space complexity??
    ans = defaultdict(list)
    for q in queries:  # O(q)
        pattern = q.replace('?', '.')  # O(M)
        for word in words:  # O(w)
            res = re.search(pattern, word)  # O(???)
            if res and res.string == word:
                ans[q].append(word)
    return ans

def sets(words: list, queries: list):
    sets = defaultdict(set)
    ans = defaultdict(set)
    for word in words:
        for i, c in enumerate(word):
            sets[i,c].add(word)

    all_words = set(words)
    for q in queries:
        possible_words = [sets[i,c] for i, c in enumerate(q) if c != "?"]
        w = reduce(set.intersection, possible_words)
        ans[q] = w
    return ans

def trie(words, queries):
    # build the trie (prefix tree)
    # in another file...
    pass

#M = 3
words = ["cat", "map", "bat", "man", "pen"]
queries = ["?at", "ma?", "?a?", "??n"]
ans = regex(words, queries)
print(ans)
