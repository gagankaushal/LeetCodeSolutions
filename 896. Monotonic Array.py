class Solution:
    def isMonotonic(self, A) -> bool:
        
        flagIncreasing = 0
        flagDecreasing = 0
            
        for i in range(0,len(A)-1):
            if A[i]<A[i+1] or A[i]==A[i+1]:
                flagIncreasing = flagIncreasing + 1
            if A[i]>=A[i+1] :
                flagDecreasing = flagDecreasing + 1
                
        if flagIncreasing == len(A)-1 or flagDecreasing == len(A)-1:
            return True

        else:
            return False
            
b = Solution()
b.isMonotonic([4,3,2,3,2,1,1])