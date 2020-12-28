class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        
        if len(nums)<3 or not nums:
            return []
        for i in range(len(nums)-2):
            # if num 
            left = i+1
            right = len(nums)-1
            target = 0
            if nums[i-1] == nums[i] and i>0:
                continue
                
            while left<right:
                
                if nums[left] + nums[right] == target-nums[i]:
                    # if nums[i] != output[-1][0] and nums[left] != output[-1][1] and nums[right] != output[-1][2]:
                    output.append([nums[i], nums[left], nums[right]])    
  
                    while (left<right and nums[left] == nums[left+1]):
                        left +=1
                    # while (left<right and nums[right] == nums[right-1]):
                    #     right +=1
                    left+=1
                    right -= 1
                        
                elif nums[left] + nums[right] < target-nums[i]:
                    left += 1
                else:
                    right -= 1
                    
        return output
