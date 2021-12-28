def preprocess(pattern: str) -> list:
        '''Preprocess pattern to construct LPS list, where
        lps[i] = the length of the longest prefix which is also a suffix of pattern[0:i+1]
        '''
        m = len(pattern)
        lps = [0]*m
        # lps[0] is 0
        i = 1
        longest_at_i = 0
        ## stuff i need to digest before writing
        # ...
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
                while j < m:
                        if text[i] != pattern[j]:
                                if j != 0:
                                        j = lps[j-1]
                                else:
                                        break
                        j += 1
                if j == m:
                        ans.append(i)
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

text = 'abcdef'
pattern = 'bcd'  # get better input
naive_ans = naive(text, pattern)
#kmp_ans = kmp(text, pattern)
print(naive_ans)
#assert(naive_ans == kmp_ans)
