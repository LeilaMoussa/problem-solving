def preprocess(pattern: str) -> list:
        '''Preprocess pattern to construct LPS list, where
        lps[i] = the length of the longest proper prefix which is also a suffix of pattern[0:i+1]
        '''
        m = len(pattern)
        lps = [0]*m
        # lps[0] is always 0
        i = 1
        longest_at_i = 0
        while i < m:
            if pattern[i] == pattern[longest_at_i]:
                # extend the prefix-suffix by one
                longest_at_i += 1
                lps[i] = longest_at_i
                i += 1
            else:
                # just because the current prefix-suffix doesn't reach i, doesn't mean it can't reach i-1
                # so shrink the possible match by one and continue
                if longest_at_i > 0:
                    longest_at_i = lps[longest_at_i - 1]
                else:
                    # but if there's nowhere to go, then this current prefix-suffix just doesn't exist
                    lps[i] = 0
                    i += 1
        return lps

def kmp(text: str, pattern: str) -> list:
    '''Given text and pattern, return all indices where pattern occurs in text'''
    n = len(text)
    m = len(pattern)

    ans = []

    lps = preprocess(pattern)

    # The general idea is to follow sliding window but optimize where matching overlaps
    # and when we already know a certain prefix matches (because we had just matched the suffix of the pattern).
    # Using LPS, skip some characters of the new window.

    i = j = 0
    while i < n:
        if text[i] == pattern[j]:
            # keep going, same as naive while matching
            i += 1
            j += 1
            if j == m:
                # you matched until and including the end of pattern
                # add to ans
                ans.append(i - m)
                # naive would reset j to 0 here
                # but the assumption is after a match, we just matched a suffix at index j - 1 (at this point, because j is past the pattern)
                # that suffix could also be a prefix that we can take for granted in the search of our next full match
                # skip the length of the prefix that is the same as suffix at index j - 1 of pattern, i.e. lps[j-1]
                # i is also past the last match too, so we're already looking at a different character of text
                j = lps[j-1]
        else:
            # naive would reset j to 0 here too
            # if text and pattern don't match, it's also possible that we just achieved a partial match -- is this relevant
            # i stays put on the character of text that just mismatched
            # j doesn't go back to 0 immediately
            # this part is missing
            # that and why the insistance on *proper* prefix, while regular suffix
            if j > 0:
                j = lps[j-1] # will ultimately go to 0 if i is truly not an answer
            else:
                i += 1
    return ans

def naive(text: str, pattern: str) -> list:
    '''Sliding window -- naive'''
    n = len(text)
    m = len(pattern)

    ans = []

    for i in range(n-m+1):
        if text[i:i+m] == pattern:
            ans.append(i)
    return ans

test_cases = [ # text, pattern, ans
    ['abdcef', 'ab', [0]],
    ['abdcefab', 'ab', [0, 6]],
    ['abababab', 'ab', [0, 2, 4, 6]],
    ['abaabaaba', 'abaa', [0, 3]],
    ['abaabaaba', 'f', []],
    ['rfff', 'ff', [1, 2]]
]
for test in test_cases:
    [text, pattern, ans] = test
    naive_ans = naive(text, pattern)
    kmp_ans = kmp(text, pattern)
    assert(naive_ans == kmp_ans)
    assert(kmp_ans == ans)
    #print(ans)
