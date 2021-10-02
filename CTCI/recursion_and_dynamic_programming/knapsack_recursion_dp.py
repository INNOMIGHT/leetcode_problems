def create_matrix(capacity, n):
    matrix = [[-1 for x in range(capacity+1)] for x in range(n+1)]
    return matrix

t = create_matrix(10, 4)
    

def knapsack_recursion_dp(capacity, weights, values, n):
    if capacity == 0 or n == 0:
        return 0
    if t[n][capacity] != -1:
        return t[n][capacity]
    else:
        if weights[n-1] <= capacity:
            t[n][capacity] = max(values[n-1]+knapsack_recursion_dp(capacity-weights[n-1], weights, values, n-1), knapsack_recursion_dp(capacity, weights, values, n-1))
            return t[n][capacity]
        elif weights[n-1] >= capacity:
            t[n][capacity] = knapsack_recursion_dp(capacity, weights, values, n-1)
            return t[n][capacity]


print(knapsack_recursion_dp(10, [1, 3, 5, 6], [20, 30, 10, 50], 4))
