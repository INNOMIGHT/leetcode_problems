class Solution:

    def check_balance(self, s):

        if len(s)%2 != 0:
            return False

        brackets = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        for char in s:
            if char in brackets.values():
                stack.append(char)
            else:
                if stack == [] or brackets[char] != stack.pop():
                    return False
        return stack == []


sol = Solution()
print(sol.check_balance("(){}"))
