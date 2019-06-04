class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        count = 0

        temp = []

        for i in heights:
            temp.append(i)

        temp.sort()

        for i in range(0, len(heights)):
            if heights[i] !=temp[i]:
                count = count + 1

        return(count)

A = Solution()
A.heightChecker([1,1,4,2,1,3])