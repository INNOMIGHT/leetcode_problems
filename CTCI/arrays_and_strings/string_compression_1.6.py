# Solution 1.6

class Solution:

    def string_compression(self, s):

        count = 1
        result_string = ""
        i = 1

        while i < len(s):
            if s[i] == s[i-1]:
                count += 1
            else:
                result_string = result_string + s[i-1] + str(count)
                count = 1
            i += 1
        
        result_string = result_string + s[i-1] + str(count)
        
        return result_string


sol = Solution()
print(sol.string_compression("aabcccccaaa"))