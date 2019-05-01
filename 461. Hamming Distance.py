class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        z =0
        s=''
        count = 0
        
        if len(bin(x)[2:]) > len(bin(y)[2:]):
            z = len(bin(x)[2:]) - len(bin(y)[2:])
            for z in range (0,z):
                s = s + '0'
            s = s + str(bin(y)[2:])
            r = str(bin(x)[2:])
        
        elif len(bin(y)[2:]) > len(bin(x)[2:]):
            z = len(bin(y)[2:])-len(bin(x)[2:])
            for z in range (0,z):
                s = s + '0'
            s = s + str(bin(x)[2:])
            r = str(bin(y)[2:])
         
        elif len(bin(y)[2:]) == len(bin(x)[2:]):
            s = str(bin(x)[2:])
            r = str(bin(y)[2:])
               
        print (s,r)
        
        for e in range (0,len(s)):
            if s[e]!=r[e]:
                
                count = count + 1
                print(s[e],r[e])        
        return(count)
        
A=Solution()
A.hammingDistance(93, 73)