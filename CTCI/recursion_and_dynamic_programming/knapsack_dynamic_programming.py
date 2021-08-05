# def knapsack_dp(capacity, weights, values):
#     matrix = [[[0, 0]]*4]

#     for i in range(capacity+1):
#         curr_capacity = i
#         for j in range(len(weights)):
#             print(i, weights[j])
#             if i >= weights[j] and matrix[i-1][1] < values[j]:
#                 matrix.append([weights[j], values[j]])
#                 curr_capacity -= weights[j]
#                 if curr_capacity >= weights[j]:
#                     new_value = matrix[len(matrix)-2][1] + values[j]
#                     print(matrix[len(matrix)-2][1], values[j], new_value)
#             else:
#                 matrix.append([weights[j], matrix[len(matrix)-1][1]])

#     print(matrix)

def knapsack_dp(capacity, weights, vals, n):
    n = len(vals)
    matrix = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    for i in range(n+1):
        for j in range(capacity+1):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif weights[i-1] <= j:
                matrix[i][j] = max(vals[i-1] + matrix[i-1][j-weights[i-1]], matrix[i-1][j])
            else:
                matrix[i][j] = matrix[i-1][j]

    print(matrix)
    



knapsack_dp(10, [1, 3, 5, 6], [20, 30, 10, 50], 4)
