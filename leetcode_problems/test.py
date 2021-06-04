subsets = []
arr = [1, 2, 3, 4]
for i in range(len(arr)):
    for j in range(i):
        subsets.append(nums[j:i])