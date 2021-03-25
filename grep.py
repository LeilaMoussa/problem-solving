def print_lines(line_num: int, context: int, text: list, last_printed: int) -> int:
    start = max(last_printed+1, line_num-context)
    start = max(start, 0)
    end = min(line_num+context, len(text)-1)
    for i in range(start, end+1):
        print(text[i])
    return end

def grep(key: str, text: list, context=0):
    '''Look for matches of key in words.
    A match happens when key occurs within a line.
    Print the matching line and the context around it
    (the number of line before and after it).
    No line can be printed more than once. ==> O(n) time.'''

    last_printed = -1
    for i, line in enumerate(text):
        if key in line:
            last_printed = print_lines(i, context, text, last_printed)

text = ['uni bookstore',
         'buy',
         'author',
         'publishing house',
         'binding',
         'al akhawayn university',
         'melon']
key = 'uni'

grep(key, text, 3)
