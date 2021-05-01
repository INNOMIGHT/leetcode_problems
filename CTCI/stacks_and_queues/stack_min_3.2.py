class Solution:

    # find the minimum element in stack in O(1) time.
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min = 0

    def push(self, item):
        if self.stack == []:
            self.min = item
            self.min_stack.append(item)
        if item < self.min:
            self.min = item
        self.stack.append(item)
        self.min_stack.append(item)


    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def stack_min(self):
        return self.min_stack[-1]


sol = Solution()
sol.push(4)
sol.push(7)
sol.push(3)
sol.push(8)
sol.push(6)
sol.push(9)
print(sol.stack_min())
