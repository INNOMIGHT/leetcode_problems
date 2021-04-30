# Solution 1.7
import time
class Solution:
    
    def rotate_matrix(self, arr):
        begin = time.time()

        n = len(arr[0])
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = arr[i][j]
                arr[i][j] = arr[n - 1 - j][i]
                arr[n - 1 - j][i] = arr[n - 1 - i][n - 1 - j]
                arr[n - 1 - i][n - 1 - j] = arr[j][n - 1 - i]
                arr[j][n - 1 - i] = temp
        
        time.sleep(1)
        end = time.time()
        runtime = end - begin
        
        return arr, runtime




sol = Solution()
print(sol.rotate_matrix([[1, 2, 3],[4, 5, 6], [7, 8, 9]]))