# Solution 1.5

class Solution:

    def one_away(self, s1, s2):
        l1 = len(s1)
        l2 = len(s2)

        if abs(l1 - l2) > 1:
            return False
        
        if l1 > l2:
            l1, l2 = l2, l1
        
        index1 = 0
        index2 = 0
        found_diff = False

        while index2 < l2 and index1 < l1:
            if s2[index2] != s1[index1]:
                if found_diff:
                    return False
                else:
                    found_diff = True
                
                if l1 == l2:
                    index1 += 1
            
            else:
                index1 += 1
            
            index2 += 1
            
        return True

sol = Solution()
print(sol.one_away("pales", "pale"))
