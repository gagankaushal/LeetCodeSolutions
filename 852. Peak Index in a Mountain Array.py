class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mountain = 0
        
        for i in range(0,len(A)-1):
            
            if A[i]<A[i+1]:
                mountain = i+1
                
        return mountain