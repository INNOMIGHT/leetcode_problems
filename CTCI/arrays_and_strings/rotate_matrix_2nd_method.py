import time


class Solution:
    def rotate(self, matrix):
        begin = time.time()
        # transpose matrix diagonally
        # exchange diagonal values
        
        n = len(matrix)
        i = 0
        j = 0
        while i < n:
            j = i
            while j < n:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j += 1
            i += 1
        
        i = 0
        j = 0

        while i < n:
            j = 0
            while j < n//2:
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
                j += 1
            i += 1
        
        time.sleep(1)
        end = time.time()
        runtime = end - begin
        return matrix, runtime


sol = Solution()
print(sol.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
