class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        if math.sqrt(num) == int(math.sqrt(num)):
            return True
        else:
            return False

A = Solution()
A.isPerfectSquare(4)