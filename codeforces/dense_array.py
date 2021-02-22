"""
this condition must be satisfied:
max(a[i],a[i+1]) / min(a[i],a[i+1]) ≤ 2
You are given an array a of n integers.
What is the minimum number of numbers you need to add to an array to make it dense? 
You can insert numbers anywhere in the array. 
If the array is already dense, no numbers need to be added.
"""


def dense_array():

    # input

    t = int(input())
    for test in range(t):
        len_arr = int(input())
        n = input().split(" ")
        arr = []
        for inp in n:
            inp = int(inp)
            arr.append(inp)

        count = 0
        for i in range(len(arr)-1):
            max_adj = max(arr[i], arr[i+1])
            min_adj = min(arr[i], arr[i+1])

            while min_adj*2 < max_adj:
                min_adj = min_adj*2
                count += 1

        print(count)


dense_array()