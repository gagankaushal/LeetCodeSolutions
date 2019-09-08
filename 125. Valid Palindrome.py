import string

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        checker = ''
        total = string.ascii_lowercase + string.ascii_uppercase + string.digits
        count = 0
        
        for i in s:
            #print string.ascii_lowercase
            if i in total:
                checker = checker + string.lower( i)
                #checker = checker
            
            #if i in
                
        for i in range(0,(len(checker))/2):
            if checker[i] == checker[len(checker)-i-1]:
                count = count + 1
            else:
                break
        
        if len(checker)%2 == 0 and count == (len(checker))/2:
            return True
        elif len(checker)%2 == 0 and count != (len(checker))/2:
            return False
        
        
        elif len(checker)%2 != 0 and count == int((len(checker))/2):
            return True
        elif len(checker)%2 != 0 and count != int((len(checker))/2):
            return False
            
             