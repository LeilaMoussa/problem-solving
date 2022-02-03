'''https://techdevguide.withgoogle.com/resources/former-interview-question-compression-and-decompression/#!
'''

def solve(s: str) -> str:
    '''
    find the current factor then recurse on the concerned string
    this would address nested repetitions
    but the question is how do you find the concerned string
    sure you could iterate before you recurse
    '''
    # I'm 100% certain there's a much nicer way to do this. I'm getting there.
    fact = ''
    paren = 0
    base = True
    ans = ''
    i = 0
    while i < len(s):
        elt = s[i]
        if elt.isdigit():
            fact += elt
            base = False
            i += 1
        elif elt == '[':
            base = False
            paren += 1
            fact = int(fact)
            j = i+1
            while j < len(s):
                if s[j] == ']':
                    paren -= 1
                elif s[j] == '[':
                    paren += 1
                if paren == 0:
                    break
                j += 1
            ans += fact * solve(s[i+1:j])
            fact = ''
            i = j+1
        elif elt == ']':
            base = False
            i += 1
        else:
            ans += elt
            i += 1
    if base:
        return s
    return ans

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
        #print("test case", i)
        x = solve(elt)
        #print("out", x)
        assert(x == _out[i])

test()
