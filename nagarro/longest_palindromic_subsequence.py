def lps(s, i, j):

    if i == j:
        return 1
    if s[i] == s[j] and i+1 == j:
        return 2
    if s[i] = s[j]:
        return 2 + lps(s, i+1, j-1)
    else:
        return max(lps(s, i+1, j), lps(s, i, j-1))


s = "bbab"
n = len(s)
print(lps(s, 0, n-1))