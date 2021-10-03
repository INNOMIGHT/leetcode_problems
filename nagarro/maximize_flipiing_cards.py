def flip_cards(arr):

    min_sum = arr[0]
    curr_sum = min_sum

    for i in range(len(arr)):
        curr_sum = min(curr_sum + arr[i], arr[i])
        min_sum = min(curr_sum, min_sum)

    
    return min_sum


print(flip_cards([-2, 3, -1, -4, -2]))