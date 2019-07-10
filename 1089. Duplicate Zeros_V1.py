class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        listOfIndexZeroes = []
        for i in arr:
            if i == 0:
                listOfIndexZeroes.append(i)


A=Solution()
A.duplicateZeros([1,0,2,3,0,4,5,0])
