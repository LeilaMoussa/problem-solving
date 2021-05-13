from random import random
from math import floor

def decide(i: int) -> bool:
    # 1/i prob to retain, 1-1/i prob to discard
    return 100*random() <= floor(100/i)

def pick_uniform(numbers) -> int:
    i = 1
    retain = True
    for curr in numbers:
        if retain: retained = curr  # always retain first
        i += 1
        retain = decide(i)
    return retained

n = int(input('Non zero positive integer\n'))
numbers = range(n)
ans = pick_uniform(numbers)
print(ans)
