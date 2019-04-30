class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #print('hi')
        count = 0
        
        N = str(n)
        
        #len
        #N = '1'+N
        
        for i in N:
            if i == '1':
                count = count + 1
            
        print (count)
        
A = Solution()
A.hammingWeight(1011)