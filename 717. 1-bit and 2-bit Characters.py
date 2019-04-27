class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        lastBitstatus = 0 # value is 1 for 1 bit, value is 2 for 2 bit
        i = 0
        
        while (i<len(bits)):
            print (i)
            if bits[i] == 0:
                lastBitstatus = 1
                i = i + 1
            else:
                lastBitstatus = 2
                i = i+2
        
	if lastBitstatus==1:
            print True
        elif lastBitstatus==2:
            return False
                    
A = Solution()
A.isOneBitCharacter([1,1,1,0,0,1,0,0])        

