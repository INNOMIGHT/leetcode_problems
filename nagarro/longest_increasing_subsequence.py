def lis(n, arr):

    dp = [1 for i in range(n+1)]
    
    for i in range(1, n):
        for j in range(0, i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
        

print(lis(7, [7,7,7,7,7,7,7]))