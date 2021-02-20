"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer
range [-231, 231 - 1], then return 0
"""


class Solution:

    def reverse(self, x: int) -> int:
        if x > 0:
            str_x = str(x)
            rev_x = str_x[::-1]
            rev_x = rev_x.lstrip('0')

            if 2**-31 < int(rev_x) > 2**31:
                return 0
            else:
                return rev_x

        elif x < 0:
            str_x = str(x)
            str_x = str_x[1:]
            rev_x = str_x[::-1]
            rev_x = rev_x.lstrip('0')

            if 2**-31 < int(rev_x) > 2**31:
                return 0
            else:
                return "-" + rev_x

        else:
            return 0


sol = Solution()
print(sol.reverse(-43300))
