class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        lastNumber = [1,1]
        
        if rowIndex== 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            
            for j in range (2,rowIndex+1): # Number of times the calcualtion has been done to find the final ans
                length = j + 1
                numberOfMissingElements = length - 2
                currentNumber = [None]*length
                currentNumber[0] = 1
                currentNumber[length-1] = 1
                
                for i in range(1,numberOfMissingElements+1):
                    currentNumber[i] = lastNumber[i-1] + lastNumber[i]
                
                lastNumber = currentNumber
            return (currentNumber)

A = Solution()
A.getRow(5)