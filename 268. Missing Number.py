class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        nums.sort()
        
        
        for i in range(0,len(nums)):
            if(i == 0):  #for first element in list
                if ( i != nums[i]):
                    missing = i
                    break
                elif(i == nums[i] and len(nums)==1):
                    missing = i+1
                    break
                
            elif (0<i<len(nums)-1): #for elements from 1 to n-1
                if nums[i] != nums[i-1] + 1:
                    missing = nums[i] - 1
                    break
       
            elif(i == len(nums)-1): #for last element in list
                if (i != nums[i]):
                    missing = nums[i] - 1
                    break
                elif (i == nums[i]):
                    missing = nums[i] + 1
                    break
       
           
            
        return(missing) 

A=Solution()
A.missingNumber([0])