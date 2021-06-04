def recursion(val):
    if val < 1:
        return 0
    return min(recursion(val-2), recursion(val-1))+1


print(recursion(5))