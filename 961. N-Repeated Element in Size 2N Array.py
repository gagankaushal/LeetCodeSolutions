class Solution:
    def repeatedNTimes(self, A) -> int:
        
        B = []
        j = 0
        for i in A:
            if i not in B:
                B.append(i)
            else:
                j = i
                break
        return (j)
               
A = Solution()
A.repeatedNTimes([1,2,3,3])
        
    