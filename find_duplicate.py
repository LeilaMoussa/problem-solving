"""
Prompt:
Given an array of n + 1 integers between 1 and n, find one of the duplicates.
If there are multiple possible answers, return one of the duplicates.
If there is no duplicate, return -1.
Example:
Input: [1, 2, 2, 3]
Output: 2
Input: [3, 4, 1, 4, 1]
Output: 4 or 1
"""

from collections import defaultdict

def find_duplicate_1(array: list) -> int:
    # Brute force.
    # O(n^2) time
    # O(1) space
    for i, elt in enumerate(array):
        if elt in array[:i]+array[i+1:]:  ## Could've just iterated simply and checked the index.
            return elt
    return -1

def find_duplicate_2(array: list) -> int:
    # Using a dictionary.
    # O(n) time
    # O(n) space
    values = defaultdict(bool)
    for elt in array:
        if values[elt]:
            return elt
        values[elt] = True
    return -1

# Approaches 1 & 2 do not make use of the properties of the array.

def find_duplicate_3(array: list) -> int:
    # Using indices, after sorting.
    # The elements are consecutive integers,
    # and the smallest element is 1
    # so each element should be one greater than its index
    # except the duplicate -- it's equal to its index

    # O(n logn) time
    # O(1) space
    array.sort()
    for i, elt in enumerate(array):
        if i == elt:
            return elt
        # Alternatively: I could compare each number to the one after it.
        # Two equal consecutive numbers => found the duplicate.
    return -1

def find_duplicate_4(array: list) -> int:
    # Using arithmetic.
    # This does not always work.
    # It only works when there is EXACTLY ONE duplicate.
    # O(n) time
    # O(1) space
    if len(array) == 0:
        return -1
    n = max(array)
    sum_to_n = n*(n+1)//2
    return sum(array) - sum_to_n

##def helper_find_first_unvisited(array: list, length: int) -> int:
##    # Helper function for find_duplicate_5() that runs in O(n) time.
##    # It finds the first unvisited (positive) element and returns its index.
##    j = 0
##    while j < length and array[j] < 0: j += 1
##    return j
    
##def find_duplicate_5(array: list) -> set:
##    # I'm returning all duplicates in this variation, for some reason...
##    
##    # Another way to use indices, different from approach 3.
##    # element A points to element B if index of element B is equal to element A.
##    # Mark each element as "visited" somehow (add a minus to preserve abs value)
##    # When you reach an element which has been previously visited, ITS INDEX is the duplicate.
##    # Downside: corrupts the initial data (if we want to be O(1) space)
##    # Of course, this only works because all the numbers are between 1 & n (n is the last index)
##    #   ==> positive and no "out of bounds".
##
##    # this one is O(n^2) time and O(n) space specifically because I am looking for all duplicates.
##    # (dups can be n/k large, right, where k is the number of occurrences of the same element? Please correct me if I'm wrong.)
##    # See next function for the actual approach
##    length = len(array)
##    i = 0
##    dups = set()
##    while i < length:
##        elt = array[i]
##        if elt < 0:
##            dups.add(i)
##            # update the index somehow to break out of the loop of pointers
##            # find the first unvisited elt? that's one way of doing it! but not good obviously
##            j = helper_find_first_unvisited(array, length)  # Bad.
##            i = j
##        else:
##            array[i] = -elt
##            if i != elt:
##                i = elt
##            else:
##                i = helper_find_first_unvisited(array, length) # Bad, but necessary to avoid infinite self-loops.
##    return dups

def actual_find_duplicate_5(array: list) -> int:  # Don't mind the previous version of 5.
    # Actual good implementation with the pointing idea.
    # This time, instead of traversing the array arbitrarily, we iterate sequentially.
    # We only return one duplicate if many exist.
    # Time: O(n), Space: O(1)
    if len(array) == 0:
        return -1
    for i, elt in enumerate(array):
        # Remember: the index is the duplicate,
        # and check whether the guy we're POINTING to is negative, not the current guy!
        # make use of absolute value
        pointed = abs(elt)
        pointed_val = array[pointed]
        if pointed_val < 0:
            return pointed
        else:
            array[pointed] = -pointed_val

def find_duplicate_6(array: list) -> int:
    # Same idea as pointers, but using Floyd's cycle finding algorithm to find cycle created by the pointers.
    # The duplicate is the entry point to the cycle.
    # This approach takes some effort to understand...
    # O(n) time, O(1) space, no data mutation.

    # Algo:
    # First loop:
    #   Move "slow" by one move at a time, and "fast" by 2 moves at a time
    #   (one move is one arrow, based on the pointer idea)
    #   Stop when slow and fast happen to be AT THE SAME CELL
    # Second loop:
    #   Reset slow (slow is index 0)
    #   Move slow & fast one move at a time EACH.
    #   By the time they're equal, they're pointing to different cells with equal values
    #   They're equal to the duplicate.

    # What I need to do: 1. understand WHY this works (why does Floyd's work?)
    #                    2. How exactly does this behave with more than one duplicate?

    if len(array) == 0:
        return -1
    slow = array[0]
    fast = array[array[0]]
    while slow != fast:
        slow = array[slow]
        fast = array[array[fast]]
    slow = 0
    while slow != fast:
        slow = array[slow]
        fast = array[fast]
    return slow

# Let n = 6, one duplicate.
array = [2, 1, 3, 4, 5, 6, 5]
ans = find_duplicate_6(array)
print(ans)
