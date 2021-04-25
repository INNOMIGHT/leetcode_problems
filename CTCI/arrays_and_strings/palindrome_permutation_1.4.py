# Solution 1.4

class Solution:

    def palindrome_permutation(self, s):
        s = s.lower()
        s = s.replace(" ", "")
        char_count = dict()
        unique_char_list = []
        for char in range(len(s)):
            char_count[s[char]] = s.count(s[char])

        for key, value in char_count.items():
            if value < 2:
                unique_char_list.append(key)

        print(char_count)
        print(unique_char_list)
        if len(unique_char_list) > 1:
            return False
        else:
            return True


sol = Solution()
print(sol.palindrome_permutation("Tact Coa"))

# Another possible solution - we dont need to count,
# we just need to know if the count is even or odd.
# At most 1 odd count and all even means its pal-perm.
