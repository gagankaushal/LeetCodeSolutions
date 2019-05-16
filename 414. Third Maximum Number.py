class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        newNums = []

        for n in nums:
            if n not in newNums:
                newNums.append(n)

        newNums.sort()

        if len(newNums) < 3:
            return newNums[len(newNums) - 1]

        else:
            return newNums[len(newNums) - 3]

A = Solution()
A.thirdMax([2, 2, 3, 1])