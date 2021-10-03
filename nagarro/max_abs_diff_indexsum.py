def max_diff(arr):
    maximum = 0

    for i in range(1, len(arr)):
        for j in range(i):
            temp_diff = abs(arr[j] - arr[i]) + abs(i - j)
            if temp_diff > maximum:
                maximum = temp_diff
    
    return maximum


print(max_diff([3, -2, 5, -4]))
