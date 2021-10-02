def sibling_search(n, arr, x):

    level = 0
    start_index = 0
    
    while start_index < n:
        end_index = pow(2, level) + start_index
        if x in arr[start_index:end_index]:
            break
        
        level += 1
        start_index = (2 * start_index) + 1

    final_array = arr[start_index:end_index]
    final_array.remove(x)

    if final_array:
        return final_array
    else:
        return -1
        

print(sibling_search(6, [1, 2, 3, 4, 5, 6], 5))