number_pad = {
    '1': ['a', 'b', 'c'],
    '2': ['d', 'e', 'f']
    }

def get_words(seq: str, prefix: str) -> list:    
    # seq can't get empty.
    digit = seq[0]
    if len(seq) == 1:
        # End of the word, just return all possible last letters.
        some_words = []
        for last in number_pad[digit]:
            some_words.append(prefix+last)
        return some_words
    output = []
    for letter in number_pad[digit]:
        returned_words = get_words(seq[1:], prefix+letter)
        # `returned_words` originates from `output` (if seq has at least 2 digits) or from `some_words`
        for elt in returned_words:
            output.append(elt)  # I could append the lists themselves then return a flattened version in the end (numpy). Might try that.
    return output

seq = '12'
ans = get_words(seq, '')
assert(len(ans) == 3 ** len(seq))
print(f'You could have typed: {ans[0]}', end='')
for possible_word in ans[1:]:
    print(',', possible_word, end='')
