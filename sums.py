"""
Two-sum, Three-sum: find a single group of 2 or 3 numbers, if applicable, at different cells, that sum up to a target.
Zero to many solutions may exist.
Subset-sum at the end.

I need to come back to finish time & space complexities.
"""

from collections import defaultdict
import sys

sort = False
prob = None

def modified_binary_search(nums: list, val: int, current_idx: int, left: int, right: int) -> int:
    # Return the index of the complement of the value we're at.
    # val means the complement we're searching for.
    # Must check though that the index is not the same!

    # Note to self: I used array slicing at first for the recursive calls,
    # but that's stupid because we're looking for the indices!

    # (This PDF (https://web.stanford.edu/class/cs9/sample_probs/TwoSum.pdf) adds something:
    # ==> Otherwise, just check the immediate neighbor cells, since nums is sorted.) <-- idk??
    if left > right:
        return -1
    mid = (left+right)//2
    mid_val = nums[mid]
    if mid_val == val:
        if mid != current_idx:
            return mid
    elif mid_val < val:
        return modified_binary_search(nums, val, current_idx, mid+1, right)
    else:
        return modified_binary_search(nums, val, current_idx, left, mid-1)

def two_sum(nums: list, target: int, is_sorted: bool) -> tuple:
    # Find a pair that sums up to a target (not necessarily 0 here).
    # They have to be different cells.
    # is_sorted means: is the array sorted in ASCENDING order?
    n = len(nums)
    if n < 2:
        return  # No answer.
    if is_sorted:
        # Version 1: use two pointers in O(n) time and O(1) space.
        left = 0
        right = n-1
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                return (left, nums[left]), (right, nums[right])
        # -------------------------------------------------------------------------------------
        # Version 2: binary search, but O(nlogn) time.
##        for i, elt in enumerate(nums):
##            comp_idx = modified_binary_search(nums, target-elt, i, 0, n-1)
##            if comp_idx >= 0:
##                return ((comp_idx, target-elt), (i, elt))
    else:
        # Use a dict in O(n) time and O(n) space.
        # version 1: dict of values
##        values = defaultdict(int)  # key: the number, value: its index
##        for i, elt in enumerate(nums):
##            values[elt] = i
##            complement = target-elt
##            if complement in values and values[complement] != i:
##                return ((i, elt), (values[complement], complement))
        # -----------------------------------------------------------------------------------
        # version 2: dict of complements
        comps = defaultdict(int)  # key: the complement, value: index of the original
        for i, elt in enumerate(nums):
            complement = target-elt
            comps[complement] = i
            if elt in comps and comps[elt] != i:
                return ((i, elt), (comps[elt], complement))

def three_sum(nums: list, target: int) -> tuple:
    # Find three numbers in an array that SUM UP TO 0.
    # Using 2 pointers.
    # O(n^2) time & O(1) space.

    # Attention: this is different from this problem: https://leetcode.com/problems/3sum/description/ (which has to take O(n^3)) !!
    # Here, I'm only looking for one triplet.
    nums.sort()
    n = len(nums)
    if n < 3:
        return
    i = 0
    while i < n:
        elt = nums[i]
        left = i+1
        right = n-1
        while left < right:
            s = elt + nums[left] + nums[right]
            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                return ((i, elt), (left, nums[left]), (right, nums[right]))
                # Ignore the following commented code. See next function.
##                while left < right and nums[left+1] == nums[left]:  ## Contiguous duplicates.
##                    left += 1
##                left += 1
        i += 1

def all_three_sums(nums: list, target: int) -> set:
    # Find all unique triplets that sum up to the target.
    # Here is where I store each valid triplet and move on,
    # which means using the code snippet above.
    # I may come back to implement this, but without repeating the previous function.
    # ==> Could I use decorators? Hmm.
    pass

def subset_sum_recursion(nums: list, target: int) -> bool:
    # Very different problem here!
    # Here's we're looking for WHETHER A SUBSET SUMS UP TO A TARGET, GIVEN A SET OF INTEGERS (list here).
    # Using recursion first, not DP.
    # The idea is that if such a subset exists, it either includes the last element or not.
    # Exponential time because it may consider all subsets. (More rigorous understanding of time complexity needed!)
    if target == 0:  # The empty set.
        return True
    elif len(nums) == 0:  # Can't form non-zero with nothing.
        return False
    return subset_sum_recursion(nums[:-1], target) or subset_sum_recursion(nums[:-1], target-nums[-1])  # Doesn't include or includes.

def subset_sum_dp(nums: list, target: int) -> bool:
    for elt in nums:
        if elt < 0:
            raise ValueError
    n = len(nums)
    # Improving the recursive solution: for each subarray nums[0:idx+1], determine if there a subset that adds up to a number,
    # and that number can be anything between 0 and the initial target!
    # ==> The integers must be positive in this case! So that the number (target minus any combination of other numbers)
    #       is definitely less than target.
    # This mean 2D array: rows mean all subarrays that start at idx 0 and
    # columns mean all possible numbers that represent the target in a particular iteration.
    # So the dimensions are: (n+1)x(target+1)
    # O(n*target) space and time ?????
    solutions = []
    for _ in range(n+1):
        solutions.append([True]+[False]*(target))
    
    # Fill the table, bottom up
    # If the current target (column) is less than the element at the current row,
    # that means that element is not in the subset
    # so the answer is whatever was the answer for the subarray right before it (and same sum of course)
    # meaning, whether that subarray returns True or False depends only on the previous subarray

    # But if the current element is less than the target,
    # We need to look at both cases:
    # included: previous subarray, and target-current_elt (previous row, another column)
    # OR excluded: previous subarray, same target (previous row, same column)
    for i in range(1, n+1):
        for j in range(1, target+1): # First column and first row are already good.
            current_elt = nums[i-1]
            if current_elt > j:  # i=0 means empty array, and i=1 means the first element only... that's why we use i-1 here
                solutions[i][j] = solutions[i-1][j]
            else:
                solutions[i][j] = solutions[i-1][j] or solutions[i-1][j-current_elt]  # Excluded or included, respectively.
    return solutions[n][target]   ## Last cell.
    
def test(nums: list, ans: tuple, target: int, prob: str) -> None:
    n = len(nums)
    if not ans:
        # I'm choosing to ignore testing this type of output because
        # I'm not sure how, without ready-to-use sample I/O or additional code.
        # Any suggestions?
        return
    if prob == '2':
        (i, elt1), (j, elt2) = ans
        statement = (i != j and 0 <= i < len(nums) and 0 <= j < len(nums) and nums[i] == elt1 and nums[j] == elt2 and elt1 + elt2 == target)
    elif prob == '3':
        (i, elt1), (j, elt2), (k, elt3) = ans
        statement = (i != j and j != k and i!= k and [0 <= x < len(nums) for x in (i, j, k)] and elt1 + elt2 + elt3 == target)
        ## idk how this loop will work
    else:
        # Also not sure how to test n-sum
        pass
    
    try:
        assert statement
        print('Success.')
    except:
        sys.stderr('Fail.')

# nums = [-1, 0, 2, -4, 1, -1]
nums = [1, 2, 5, 3]
target = 11

if sort:
    nums.sort()
if prob == '2':
    ans = two_sum(nums, target, sort)
elif prob == '3':
    ans = three_sum(nums, target)
else:
    ans = subset_sum_dp(nums, target)
print(ans)
if prob == '2' or prob == '3': test(nums, ans, target, prob)
