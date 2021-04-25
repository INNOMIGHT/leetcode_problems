# Solution 1.2
# Case sensitive and whitespace significant

class Solution:

    def check_permutation(self, s1, s2):
        if len(s1) != len(s2):
            return False
        s1_list = []
        for char in s1:
            s1_list.append(char)
        for char_s2 in s2:
            if char_s2 not in s1_list:
                return False
        return True


sol = Solution()
print(sol.check_permutation("dog   ", "   Dog"))
