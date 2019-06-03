class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        finalAns = []
        
        for i in A:
            if i%2 == 0:
                
                finalAns.append(i)
                
                
        for i in A:
            if i%2 != 0:
                
                finalAns.append(i)
                
        return finalAns