class Solution:
    def findComplement(self, num: int) -> int:
        
        b = bin(num)[2:]
        c = ''
        
        for i in range (0,len(b)):
            c = c + '1'
            
        B=int(b)
        C=int(c)
        D= str(C-B)
        e = 0
        
        for j in range (0, len(D)):     
            e = e + int(D[len(D)-j-1])*(2**j)
          
        #print (b,c,D,e)
        return (e)
        
A=Solution()
A.findComplement(7)