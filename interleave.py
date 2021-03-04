def interleave(s1: str, s2: str) -> str:
    ans = ''
    n1, n2 = len(s1), len(s2)
    if n1 == 0:
        return s2
    if n2 == 0:
        return s1
    i = j = 0 
    while i < n1 and j < n2:
        ans += s1[i] + s2[j]
        i += 1
        j += 1
    if i < n1:
        ans += s1[i:]
    elif j < n2:
        ans += s2[j:]
    return ans

s1 = ''
s2 = 'abcd'
ans = interleave(s1, s2)
print(ans)
