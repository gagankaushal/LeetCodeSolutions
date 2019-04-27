class Solution:
    def minMoves(self, nums) -> int:

        count = 0
        nums.sort()
        
        while (nums[0]!=nums[len(nums)-1]):
                                            #Find 2 minimum value elements
            #nums[0] = nums[0] + 1           # Increment these 2 elements   
            #nums[1] = nums[1] + 1           # Check whether all elements are equal
            
	    
            for i in range(0,len(nums)-1):
                nums[i] = nums[i] + 1
                print (nums)
            
            count = count + 1
            nums.sort()
        
        return (count)

A = Solution()
A.minMoves([1,1,2147483647])         
A.minMoves([1,1,2,3,3])
A.minMoves([1,4,4,6,9,9])
A.minMoves([5,6,8,8,5])
A.minMoves([1,2,3])