# Solution 1.3

class Solution:

    def urlify(self, s):

        s = s.rstrip()
        s = s.replace(" ", "%20")

        return s


sol = Solution()
print(sol.urlify("Mr John Smith    "))
