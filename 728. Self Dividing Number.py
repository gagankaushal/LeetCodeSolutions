class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
               
        final = []
                
        for i in range (left, right+1):
            l = []    
            flag = 0
                
            j = i
            while (j>0):
                
                p = j%10 
                
                l.append(p)
                
                j = j//10
            
                
            for k in l:
                if k!=0:
                    if ((i%k)!=0):
                        flag = 1
                        
                        break
                else:
                    flag = 1
                    break
                                 
            if (flag == 0):
                final.append(i)
            
        return (final)

A = Solution()
A.selfDividingNumbers(1, 22) 