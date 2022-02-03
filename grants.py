def find_grants_cap(grantsArray, newBudget):
    '''New array contains new grants.
Sum of new_grants is newBudget.
Max(new_grants) = cap
We want to maximize the number of new grants that stay the same.
From each old grant, we substract x[i] which could be 0 to get the new.
In the example:
(2-0) + (100-53) + (50-3) + (120-73) + (1000-953) = 190
The question "how do we get x[i]?" is equivalent to the question "how do we get cap?"
One way to start navigating the repartition of newBudget is to first divide it equally over all grants.
n = len(grantsArray)
avg_grant = newBudget / n
n = 5
avg_grant = 38
2 < 38, keep 2, now surplus is 36
The 4 others are greater than 38
Now we divide 190-2 by 4, giving 47.
But how does dividing ensure that the minimum number of grants are impacted?
Let's take for example 51 as a cap, this would reduce to dividing (190-2-51) by 3
but that doesn't make any sense if you follow through with it, I think
Let's try that
'''
    avg = newBudget / len(grantsArray)
    surplus = 0
    n = 0
    for elt in grantsArray:
        if elt <= avg:
            surplus += elt
        else:
            n += 1
    print(surplus)
    print(n)
    return (newBudget - surplus) / n

def test():
    _in = [
        ([2, 100, 50, 120, 1000], 190),
        ([2, 4], 3)
        ]
    _out = [
        47,
        1.5
        ]
    # i really wish i had the other test cases
    assert(len(_in) == len(_out))
    for i, (arr, budg) in enumerate(_in):
        assert(find_grants_cap(arr, budg) == _out[i])

test()
