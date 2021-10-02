def min_abs_diff(arr):

    arr = sorted(arr)
    total = 0
    total += abs(arr[0] - arr[1])
    total += abs(arr[-1] - arr[-2])

    for i in range(1, len(arr)-1):
        total += min(abs(arr[i]-arr[i-1]), abs(arr[i]-arr[i+1]))
    
    return total


print(min_abs_diff([12, 10, 15, 22, 21, 20, 1, 8, 9]))