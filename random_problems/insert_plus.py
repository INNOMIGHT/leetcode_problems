class Solution:

    def insert_plus(self, s):
        x = s.split("=")[0]
        y = s.split("=")[1]
        print(type(x), y)
        count = 0

        if x == y:
            return count

        x_len = len(x)
        y_len = len(y)

        # 111 = 12
        j = 0
        for i in range(x_len):
            i=j
            if i >= len(x):
                break
            if x[i:y_len+i] < y and i <= x_len - y_len :
                j = i + len(y)
            else:
                j = i + y_len - 1

            count += 1
                
        return count-1
            

sol = Solution()
print(sol.insert_plus("11789=98"))

        