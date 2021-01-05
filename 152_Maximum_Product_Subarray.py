class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxSoFar = nums[0]
        minSoFar = nums[0]
        product = nums[0]
        
        for i in range(1,len(nums)):
            tempMaxSoFar = max(nums[i], maxSoFar*nums[i], minSoFar*nums[i])
            minSoFar = min(nums[i], maxSoFar*nums[i], minSoFar*nums[i])
            maxSoFar = tempMaxSoFar 
            product = max(product, maxSoFar)
        return product
        
