class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        k = ''
       
            
        for i in range (0,len(s)):
            
            k = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = k
            s[i]=s[i-1]
            
        
A=Solution()
A.reverseString(["h","e","l","l","o"])
            