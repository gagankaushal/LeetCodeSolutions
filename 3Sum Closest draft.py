class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        diff = 1000
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    
                    #if sum - target > nums[i] + nums[j] + nums[k]:
                     #   sum = nums[i] + nums[j] + nums[k]
                    
                    if target >=0:
                        
                        if target - (nums[i] + nums[j] + nums[k])  < diff:
                            sum = nums[i] + nums[j] + nums[k]
                            diff = target - (nums[i] + nums[j] + nums[k])
                            print (nums[i],nums[j],nums[k],diff)
                    
                    else:
                        diff = -1000
                        if target - (nums[i] + nums[j] + nums[k])  > diff:
                            sum = nums[i] + nums[j] + nums[k]
                            diff = target - (nums[i] + nums[j] + nums[k])
                            print (nums[i],nums[j],nums[k],diff)
                        
                      #  sum = (nums[i] + nums[j] + nums[k])
                        
        return sum