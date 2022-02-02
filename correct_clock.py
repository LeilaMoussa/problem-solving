'''Given two 24-H format times as strings,
return the minimum number of moves required to transform time1 to time2
using a combination of only the 4 following moves:
- move forward by 5m
- move forward by 15 mn
- move forward by 30mn
- move forward by 1hr (60mn)
time1 does not necessarily occur before time2.
'''

def solve():
    pass

def test():
    _in = []
    _out = []
    assert(len(_in) == len(_out))
    for i, elt in enumerate(_in):
        assert(solve(elt) == _out[i])

test()
