import string
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        
        listOfAvailablePositions = []
        listOfNotAvailablePositions = []
        
        BufferList = []
        
        for i in range(0,len(S)):
            if S[i] in string.ascii_letters:
                listOfAvailablePositions.append(i)
            else:
                listOfNotAvailablePositions.append(i)
        
        for i in range(0, len(S)): # initializes the BufferList to the same length as the input string S
            BufferList.append('*')
            
        for i in  listOfNotAvailablePositions:
            BufferList[i] = S[i]
            
        for i in range(0,len(listOfAvailablePositions)):
            BufferList[listOfAvailablePositions[i]] = S[listOfAvailablePositions[len(listOfAvailablePositions)-i-1]]
       
        return(''.join(BufferList))
        
A=Solution()
A.reverseOnlyLetters("Test1ng-Leet=code-Q!")