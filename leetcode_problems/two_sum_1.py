""" Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target. You may assume that each input would have exactly one solution,
and you may not use the same element twice. You can return the answer in any order. """


class Solution:

    def two_sum(self, nums, target):

        seen = list()

        for num in range(len(nums)):
            difference = target - nums[num]

            if difference not in seen:
                seen.append(nums[num])
            else:
                return num, nums.index(difference)


sol = Solution()
print(sol.two_sum([9, 2, 3, 4, 5, 1], 4))



