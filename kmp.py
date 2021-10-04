def preprocess(pattern: str) -> list:
	'''Preprocess pattern to construct LPS list'''
	pass

def kmp(text: str, pattern: str) -> list:
	'''Given text and pattern, return all indices where pattern occurs in text'''
	n = len(text)
	m = len(pattern)

	lps = preprocess(pattern)

	# The general idea is to follow sliding window but optimize where matching overlaps
	# and when we already know a certain prefix matches (because we had just matched the suffix of the pattern).
	# Using LPS, skip some characters of the new window.

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