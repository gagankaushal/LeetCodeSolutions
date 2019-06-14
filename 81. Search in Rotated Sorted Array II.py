class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        found = 0
        indexFound = 0

        
        for i in range(0,len(nums)):
            if nums[i] == target:
                found = 1
                indexFound = i
                break
                
        
        if found == 1:
            return True
        else:
            return False
            
        
        