# knapsack
def literary_competition(n, t, points_arr, time_arr):

    # base_case
    if t == 0 or n == 0:
        return 0
    
    # choices
    else:
        if t < time_arr[n-1]:
            return literary_competition(n-1, t, points_arr, time_arr)
        if time_arr[n-1] <= t:
            return max(
                (points_arr[n-1] + literary_competition(n-1, t-time_arr[n-1], points_arr, time_arr)),
                (literary_competition(n-1, t, points_arr, time_arr))
                )


print(literary_competition(3, 7, [2, 6, 9], [3, 5, 3]))

