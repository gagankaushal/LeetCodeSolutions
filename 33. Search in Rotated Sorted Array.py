class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        found = 0
        indexFound = 0

        
        for i in range(0,len(nums)):
            if nums[i] == target:
                found = 1
                indexFound = i
                
        
        if found == 1:
            return indexFound
        else:
            return (-1)
            
        