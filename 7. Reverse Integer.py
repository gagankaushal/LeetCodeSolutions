class Solution:
    def reverse(self, x: int) -> int:


        X = abs(x)
        St = str(X)
        leng = len(St)
        buffer = ''


        for i in range(len(St)-1,-1,-1):
            buffer = buffer + St[i]


        if int(buffer) > ((2**31) -1):
            
            return 0
        elif  x<0:
            return (int('-'+buffer))

        elif x>=0:
            return (int(buffer))


A = Solution()
A.reverse(1534236469)
