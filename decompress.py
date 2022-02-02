'''https://techdevguide.withgoogle.com/resources/former-interview-question-compression-and-decompression/#!
'''

# A problem involving "strings, recursion, algorithm, compilers, automata, and loops."
def solve(s: str) -> str:
    pass

def test():
    _in = [
        '3[abc]4[ab]c',
        '10[a]',
        '2[3[a]b]',
        ]
    _out = [
        'abcabcabcababababc',
        'aaaaaaaaaa',
        'aaabaaab',
        ]
    assert(len(_in) == len(_out))
    for i, elt in enumerate(_in):
        assert(solve(elt) == _out[i])

test()
