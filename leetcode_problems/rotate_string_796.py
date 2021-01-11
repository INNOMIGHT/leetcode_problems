""" We are given two strings, A and B. A shift on A consists of taking string A
and moving the leftmost character to the rightmost position.
For example, if A = 'abcde', then it will be 'bcdea' after one shift on A.
Return True if and only if A can become B after some number of shifts on A."""


class Solution:

    def rotate_string(self, a, b):

        i = 0

        if a == b:
            return True

        while(i != len(a)):
            a = a[1:] + a[0]
            if a == b:
                return True

        return False


sol = Solution()
print(sol.rotate_string('abcde', 'cdeab'))
