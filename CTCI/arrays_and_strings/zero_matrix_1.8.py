# Solution 1.8

class Solution:

    def zero_matrix(self, matrix):
        n = len(matrix)
        exception = []
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0 and i not in exception and j not in exception:
                    for k in range(n):
                        matrix[i][k] = 0
                        matrix[k][j] = 0
                    exception.append(i)
                    exception.append(j)

        return matrix


sol = Solution()
print(sol.zero_matrix([[1, 0, 3], [4, 5, 6], [7, 8, 9]]))
