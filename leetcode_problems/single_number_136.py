"""
Given a non-empty array of integers nums, 
every element appears twice except for one. 
Find that single one.

Follow up: Could you implement a solution 
with a linear runtime complexity and without using extra memory?
"""

class Solution:

    def single_number(self, nums):
        count_dict = dict()
        for i in nums:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        for num in count_dict:
            if count_dict[num] == 1:
                return num

    
    



sol = Solution()
print(sol.single_number([1, 2, 2, 3, 3, 1, 7]))