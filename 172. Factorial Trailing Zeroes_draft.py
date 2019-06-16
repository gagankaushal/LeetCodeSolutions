class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        found = 0
        m =1
        '''
        def fact(i):
            if i == 1:
                return 1
            elif i == 0:
                return 1
            else:
                return (i * fact(i - 1))
        '''

        for i in range (1,n+1):
            m = m*i

        k = str(m)

        for i in range(len(k)-1,-1,-1):
            if k[i] != '0':
                break

            else:
                found = found + 1

        print(found)

        print(k)


C = Solution()
C.trailingZeroes(8979)