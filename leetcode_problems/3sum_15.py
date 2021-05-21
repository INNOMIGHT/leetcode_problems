# Given an integer array nums,
# return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.

class Solution:

    def three_sum(self, nums):
        subsets = [[]]
        result = []
        for i in range(len(nums)+1):
            for j in range(i):
                subsets.append(nums[j: i])

        for sets in subsets:
            if len(sets) == 3 and sum(sets) == 0:
                print(sets)
                result.append(sets)

        return result


sol = Solution()
print(sol.three_sum([-1,0,1,2,-1,-4]))

