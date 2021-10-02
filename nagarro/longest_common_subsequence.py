# Recursion for longest common subsequence
# def lcs(string_1, string_2, n, m):

#     # base condition
#     if n == 0 or m == 0:
#         return 0

#     # choices
#     else:
#         if string_1[n-1] == string_2[m-1]:
#             return 1 + lcs(string_1, string_2, n-1, m-1)
#         else:
#             return max(
#                 lcs(string_1, string_2, n, m-1),
#                 lcs(string_1, string_2, n-1, m-1)
#             )


# print(lcs("abcdgh", "abedfhr", 6, 7))

# Memoization for longest common subsequence (adding dp)

def lcs_helper(string_1, string_2, n, m):
    t = [[-1 for i in range(m+1)] for j in range(n+1)]
    return lcs(string_1, string_2, n, m, t)

def lcs(string_1, string_2, n, m, t):

    # base condition
    if n == 0 or m == 0:
        return 0
    if t[n][m] != -1:
        return t[n][m]
    # choices
    else:
        if string_1[n-1] == string_2[m-1]:
            t[n][m] = 1 + lcs(string_1, string_2, n-1, m-1, t)
            return t[n][m]
        else:
            t[n][m] = max(
                lcs(string_1, string_2, n, m-1, t),
                lcs(string_1, string_2, n-1, m, t)
            )
            return t[n][m]


print(lcs_helper("abcdgh", "abedfhr", 6, 7))