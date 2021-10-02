def lcs_vowel(s1, s2, m, n):
    t = [[-1 for i in range(n+1)] for j in range(m+1)]
    vowels = ['a', 'e', 'i', 'o', 'u']
    return lcs_vowel_helper(s1, s2, m, n, t, vowels)

def lcs_vowel_helper(s1, s2, m, n, t, vowels):

    # base condition
    if m == 0 or n == 0:
        return 0
    if t[m][n] != -1:
        return t[m][n]
    else:
        if s1[m-1] == s2[n-1] and s1[m-1] in vowels:
            t[m][n] = 1 + lcs_vowel_helper(s1, s2, m-1, n-1, t, vowels)
            return t[m][n]
        else:
            t[m][n] = max(lcs_vowel_helper(s1, s2, m-1, n, t, vowels), lcs_vowel_helper(s1, s2, m, n-1, t, vowels))
            return t[m][n]


print(lcs_vowel('prepinsta', 'prepare', 9, 7))
