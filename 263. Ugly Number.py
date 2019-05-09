class Solution:
    def isUgly(self, num: int) -> bool:

        rem2 = 0
        rem3 = 0
        rem5 = 0

        if num == 0:
            return False

        else:

            while num%2 == 0:
                rem2 = num%2
                num = num/2

            while num%3 == 0:
                rem3 = num % 3
                num = num / 3

            while num%5 == 0:
                rem5 = num % 5
                num = num / 5

            if num !=1:
                return False

            else:
                return True
  

A=Solution()
A.isUgly(0)
