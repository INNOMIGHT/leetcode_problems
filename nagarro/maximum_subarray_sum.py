# Brute Force - Pick out all subarrays sum and return the max sum
# Algorithm - Kadane's Algorithm, Dynamic Programming
import sys

def max_subarray(arr):

    max_sum = -sys.maxsize
    current_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(current_sum + arr[i], arr[i])
        max_sum = max(current_sum, max_sum)
    return max_sum


print(max_subarray([-2, 2, 5, -11, 6]))
