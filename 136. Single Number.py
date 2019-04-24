class Solution:
    def singleNumber(self, nums) -> int:
      
        j = {}
        j = dict.fromkeys(nums,0)
        
        for i in nums:   
            j[i]= j[i]+1
        
        for k in j.keys():
            if j[k] == 1:
                return (k) 
                break

A=Solution()
#A.singleNumber([2,2,1])
A.singleNumber([2,2,1,1,3,2,3,4])