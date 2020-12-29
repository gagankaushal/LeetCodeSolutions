class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        # start from right
        # make the indexes as right
        
        lastGoodPosition = len(nums) - 1
        
        curPos = len(nums) - 2
        while curPos >= 0:     
            if curPos + nums[curPos] >= lastGoodPosition:
                lastGoodPosition = curPos
            curPos -= 1
        if lastGoodPosition == 0:
            return True
        else:
            return False
            
