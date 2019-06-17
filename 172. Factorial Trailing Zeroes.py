import math

class Solution:
    def trailingZeroes(self, n: int) -> int:

        
        answer = 0
        i = 5

        while (math.floor(n/i)>0):
            answer = answer + math.floor(n/i)
            i = i*5

        return(answer)
