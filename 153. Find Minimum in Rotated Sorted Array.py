class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        k = 1000
        
        for i in range (0, len(nums)):
            if k>nums[i]:
                k = nums[i]
                
        return k 
                
            
        