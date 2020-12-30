class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        def formatAns(lower, upper):
            if lower == upper:
                return str(lower)
            else:
                return str(lower)+"->"+str(upper)
            
        if len(nums)==0:
            return [formatAns(lower, upper)]
        

          
        missingRanges = []
            
        if nums[0]>lower:
            missingRanges.append(formatAns(lower, nums[0]-1))
        
      
        
        for index in range(len(nums)-1):
            if nums[index+1] - nums[index] > 1:
                missingRanges.append(formatAns(nums[index]+1, nums[index+1]-1))
        
        if nums[-1] < upper:
            missingRanges.append(formatAns(nums[-1]+1, upper))
    
        return missingRanges
