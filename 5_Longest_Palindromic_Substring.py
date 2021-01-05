class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def traverseOutwards(s,left,right)-> int:
            if left>right or not s:
                return 0
            while(left>=0 and right <len(s) and s[left]==s[right]):
                left -= 1
                right += 1
            return right-left-1
        if not s:
            return ""
        start = 0
        end = 0
        
        for i in range(len(s)):
            length1 = traverseOutwards(s,i,i)
            length2 = traverseOutwards(s,i,i+1)
            
                
            print(length1, length2)
            length = max(length1, length2)
            if length> end-start:
                start = i - (length-1)//2
                end = i + length//2
        return s[start:end+1]
            
