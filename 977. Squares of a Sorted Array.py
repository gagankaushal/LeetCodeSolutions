class Solution:
    def sortedSquares(self,A) -> int:
        
        j = []
        for i in A:
            j.append(i*i)
            
        
        
        j.sort()
        return (j)
        
b = Solution()
b.sortedSquares([-4,-1,0,3,10])