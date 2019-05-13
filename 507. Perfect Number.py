import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        #num = abs(num)
        sum = 0
        
        
        if num<=1:
            return False
        
        else:
            for i in range(1, int(math.sqrt(num))+1):
             #   print(i)
                if num % i == 0:
                    sum = sum + i + num/i
    
            #print(sum,num)
        if sum-num == num:
            #print('T')
            return True

        else:
            #print('F')
            return False


A=Solution()
A.checkPerfectNumber(-6)