class Solution:
    def minMoves(self, nums) -> int:
        
        sum = 0
        numberOfWays = 0

        nums.sort()
        
        for i in range(0,len(nums)):
            sum = sum + nums[i]  
        
        numberOfWays = sum - len(nums)*nums[0]
        
        return (numberOfWays)
        
A = Solution()
A.minMoves([1,1,2147483647])         
A.minMoves([1,1,2,3,3])
A.minMoves([1,4,4,6,9,9])
A.minMoves([5,6,8,8,5])
A.minMoves([1,2,3])
