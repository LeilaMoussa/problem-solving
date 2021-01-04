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
        if elt in array[:i]+array[i+1:]:
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
    n = max(array)
    sum_to_n = n*(n+1)//2
    return sum(array) - sum_to_n

def find_duplicate_5(array: list) -> int:
    # Another way to use indices, different from approach 3.
    # element A points to element B is index of element B is equal to element A.
    # Mark each element as "visited" somehow (adding a minus here to preserve abs value)
    # When you reach an element which has been previously visited, it is the duplicate.
    

# Let n = 6
array = [2, 1, 3, 4, 5, 6, 5]
ans = find_duplicate_(array)
print(ans)
