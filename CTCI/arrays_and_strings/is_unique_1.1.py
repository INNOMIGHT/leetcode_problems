# 1.1 Solution

class Solution:

    def is_unique(self, s):
        list_of_char = []
        for char in s:
            if char in list_of_char:
                return False
            list_of_char.append(char)
        return True


sol = Solution()
print(sol.is_unique("saws"))