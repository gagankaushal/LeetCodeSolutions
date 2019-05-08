class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        a = 0
        b = 0
        flag = 0
        for i in range(int(c / 3), int(c / 2)+2):
            for j in range(0, int(c / 2)+2):
                if i * i + j * j == c:
                    a = i
                    b= j
                    flag =1
                    break
                
        if flag== 0:
            return False
        else:
            return True