def nthprime(n):
    if n == 1:
        return 1
    i = 3
    c = 1
    #print(i,c)
    while c < n:
        #print(c)
        for j in range(2,i):
            if i % j == 0:
                break
        if j == i - 1:
            c += 1
            #print(c)
        if c == n:
            return i
        i = i + 1
    return i

print(nthprime(9855523447))

# def nth_prime(n):
#     counter = 0
#     tmp_counter = 0
#     divisor_list = [2, 3, 4, 5, 6, 7, 8, 9]
#     prime_list = [1, 2, 3, 5, 7]
#     i = 1
#     if n < 5:

#     while counter != n:
#         for divisor in divisor_list:
#             if i % divisor == 0:
#                 tmp_counter += 1
#         if tmp_counter == 0:
#             counter += 1
#         tmp_counter = 0
    
#     return counter


# print(nth_prime())

