def knapsack_recursive(capacity, weights, values, n):
    # base_case
    if n == 0 or capacity == 0:
        return 0
    # choice_diagram_code
    else:
        if weights[n-1] <= capacity:
            return max(values[n-1]+knapsack_recursive(capacity-weights[n-1], weights, values, n-1), knapsack_recursive(capacity, weights, values, n-1))
        else:
            return knapsack_recursive(capacity, weights, values, n-1)


print(knapsack_recursive(10, [1, 3, 5, 6], [20, 30, 10, 50], 4))