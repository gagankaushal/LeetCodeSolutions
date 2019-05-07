class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        minu = 0

        for i in range(0,len(nums)-1,2 ):
            minu = minu + min(nums[i], nums[i + 1])
            
        return(minu)

A = Solution()
A.arrayPairSum([1,4,3,2,0,1])