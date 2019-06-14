class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        mountain = 0
        
        for i in range(0,len(nums)-1):
            
            if nums[i]<nums[i+1]:
                mountain = i+1
                
        return mountain
        