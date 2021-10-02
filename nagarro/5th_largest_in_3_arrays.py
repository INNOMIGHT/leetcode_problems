import time

start = time.time()
def fifth_largest(arr_1, arr_2, arr_3):


    new_arr = arr_1 + arr_2 + arr_3
    new_arr = sorted(new_arr)

    return new_arr[-5]

print(fifth_largest([1, 3, 5, 6, 9], [4, 6, 7, 7, 8], [2, 5, 6, 7, 8]))
end = time.time()
print("%s seconds" % (end - start))
