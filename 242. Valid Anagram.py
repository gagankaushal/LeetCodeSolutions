class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        
        S = list(s)
        T = list(t)
        S.sort()
        T.sort()
        
        if S == T:
            return True
        else: 
            return False
        