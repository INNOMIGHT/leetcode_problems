def ways_to_pay(n, count):

    # types of coins = 1, 2, 5, 10
    # base case
    if n < 0:
        return 0
    if n == 0:
        count += 1
        return count
    else:
       return ways_to_pay(n-1,count), ways_to_pay(n-2, count), ways_to_pay(n-5, count), ways_to_pay(n-10, count)



print(ways_to_pay(4, 0))
