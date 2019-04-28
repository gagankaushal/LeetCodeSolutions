class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        count = 0
        if x < 0:
            return False
        
        else:
            X = str(x)
            for i in range(0, int(len(X)/2)):
                if X[i] == X[len(X)-i-1]:
                    count = count + 2
        
        if len(X) %2 != 0:
            if count == len(X) - 1:
                return True
            else:
                return False

        else:
            if count == len(X) :
                return True
            else:
                return False
                 
                    
A = Solution()
A.isPalindrome(22321)