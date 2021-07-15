import time

def setup(n):
    start_time = time.time()
    memo = [-1] * (n+1)
    return triple_step(n, memo)


def triple_step(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    memo[n] = triple_step(n-1, memo) + triple_step(n-2, memo) + triple_step(n-3, memo)
    return memo[n]


print(setup(3))

    