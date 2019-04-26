class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        listOfZeroPositions = []
        buffer = 0
        
        for i in range(0, len(nums)):
            if nums[i] == 0:
                listOfZeroPositions.append(i)
        
        for i in range(len(listOfZeroPositions)-1,-1,-1): # picking up 0 one by one from right side from (listOfZeroPositions)
   
            for k in range(0,len(nums)-listOfZeroPositions[i]-1-(len(listOfZeroPositions)-i-1)):  #Number of swaps required = distance of 0 from right side - number of zeroes already placed on right side  
                nums[listOfZeroPositions[i]+k],nums[listOfZeroPositions[i]+1+k] = nums[listOfZeroPositions[i]+1+k],nums[listOfZeroPositions[i]+k]

A = Solution()
A.moveZeroes([0,1,2,0,2,0,4,0,0,3,12])
                
