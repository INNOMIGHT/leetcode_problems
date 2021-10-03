def coin_change(coin_arr, length, n, t):

    if n < 0:
        return 0

    if t[length][n] != 0:
        return t[length][n]

    if n == 0:
        t[length][n] = 1
        return t[length][n]

    if length <= 0 and n >= 1:
        return 0

    t[length][n] = (coin_change(coin_arr, length-1, n, t) + coin_change(coin_arr, length, n-coin_arr[length-1], t))
    return t[length][n]

coin_arr = [1, 2, 5, 10]
length = len(coin_arr)
n = 40
t = [[0 for i in range(n+1)] for j in range(length+1)]
print(coin_change(coin_arr, length, n, t))