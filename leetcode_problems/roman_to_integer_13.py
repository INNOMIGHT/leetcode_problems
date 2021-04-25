"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


class Solution:

    def roman_to_integer(self, s):
        tmp = 0
        for letter in range(len(s)):

            if s[letter] == "I":
                tmp += 1
            if s[letter] == "V":
                tmp += 5
                if s[letter-1] == "I" and letter != 0:
                    tmp -= 2
            if s[letter] == "X":
                tmp += 10
                if s[letter-1] == "I" and letter != 0:
                    tmp -= 2
            if s[letter] == "L":
                tmp += 50
                if s[letter-1] == "X" and letter != 0:
                    tmp -= 20
            if s[letter] == "C":
                tmp += 100
                if s[letter-1] == "X" and letter != 0:
                    tmp -= 20
            if s[letter] == "D":
                tmp += 500
                if s[letter-1] == "C" and letter != 0:
                    tmp -= 200
            if s[letter] == "M":
                tmp += 1000
                if s[letter-1] == "C" and letter != 0:
                    tmp -= 200
            print(s[letter] + ": ", tmp)

        return tmp
            
            
sol = Solution()
print(sol.roman_to_integer("MMMCDXC"))