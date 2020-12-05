from collections import defaultdict

def string2dict_alt(s: str) -> dict:
    """
    Remember we need to get the index that's just greater than the one before.
    Instead of searching for it, we can directly access it if we construct the arrays
        of size len(s), such that array[i] > i if the character occurs at position array[i] of s
        return -1 if the dictionary entry is not a subsequence of S
    """
    # Keep track of the index of the left-most -1 in each array
    left_most_empties = defaultdict(int)
    s_dict = defaultdict(lambda : [-1]*len(s))
    for i, char in enumerate(s):
        idx = left_most_empties[char]
        if i == 0:
            s_dict[char][-1] = i  # when prev_idx is -1, i get 0
        else:
            s_dict[char][idx:i] = [i]*(i-idx)
        left_most_empties[char] = i
    return s_dict

def string2dict(s: str) -> dict:
    s_dict = defaultdict(list)
    for i, char in enumerate(s):
        s_dict[char].append(i)
    return s_dict

def veb_tree_search():
    # for log log N search
    # i need to implement the veb class in another file
    # and figure out how to use it efficiently
    # think data population
    pass

def regularScan(arr, elt) -> int:
    for idx in arr:
        if idx > elt:
            return idx
    return -1

def binarySearchGreater(arr, elt) -> int:
    if len(arr) == 1:
        if arr[0] > elt:
            return arr[0]
        return -1
    mid = int(len(arr)/2)-1
    # I added -1 to avoid the case of arr=[6,7] and elt=5 for example (infinite recursion).
    if arr[mid] > elt:
        return binarySearchGreater(arr[:mid+1], elt)
    else:
        return binarySearchGreater(arr[mid+1:], elt)

def approach_1(s: str, d) -> str:
    """
    Represent S as a dict
    All characters in each word in D must appear in the same order as they do in S
    To keep track, look at the previous character's idx and check if it's greater than it
    To search for an index greater than the previous index: find the FIRST element greater than the previous, not just any
    That's important to account for consecutive identical characters
    
    Time complexity: O(N + L*log(N)) where L is the total number of CHARACTERS in D
    """
    #s_dict = string2dict(s)
    s_dict = string2dict_alt(s)
    longest = ''
    for entry in d:
        print("I'm at entry", entry)
        length = len(entry)
        prev_occur_idx = -1
        for i, char in enumerate(entry):
            if char in s_dict.keys():
                #res = binarySearchGreater(s_dict[char], prev_occur_idx)
                res = s_dict[char][prev_occur_idx]
                print("res", res)
                # res = regularScan(s_dict[char], prev_occur_idx)
                # res = veb_tree_search()
                if res >= 0:
                    prev_occur_idx = res
                else:
                    break
            else:
                break       
            if i == length - 1 and length > len(longest):
                longest = entry
    return(longest)

def approach_2(string, d) -> str:
    # big problem that should not happen: consecutive identical characters in an entry
    # that may go over the number of occurrences of that character in S
    
    """
    Sort dictionary entries from longest to shortest
    Look for the characters of each entry in S, in order
    Return the first subsequence found
    
    Time complexity: O(WlogW + W*N) = O(W*N) where W is # of elts in D and N is # of chars in S
    Not very good if S is much longer than the individual dictionary entries
    """
    d.sort(reverse=True, key=lambda word : len(word))
    for entry in d:
        for j, char in enumerate(entry):
            s = string
            found = False
            for i, elt in enumerate(s):
                if elt == char:
                    s = s[i+1:]
                    found = True
                    break
            if not found:
                break
            if j == len(entry) - 1:
                return entry

def approach3(s: str, d) -> str:
    """
    Exactly the same as approach 1, but with a different dict representation of s and no need to search in the middle
    Time complexity: O(N+L)
    Drawback: there are as many entries in s_dict as letters in the alphabet -> only suitable for small alphabets
    Question: why do we need that many s_dict items? Why not the same as before
    """
    #s_dict = string2dict_alt(s) # magic is in the preprocessing
    # same approach1

s = 'abppplee'
# s_dict = {'a': [0], 'b': [1], 'p': [2,3,4], 'l': [5], 'e': [6,7]}
d = ['able', 'ale', 'appleee', 'kangaroo', 'bale']
print(approach_1(s, d))
# print(approach_2(s, d))
