class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        

        flag = 0
        
        if n !=0 and n>0:
            
            while n >1:
                if n%3!=0:
                    flag = 1
                    break
        
                n = n/3
        
        elif n == 0:
            flag = 1
        
        elif -1>n:
            flag = 1 
        
        elif -1<n<0:
            #n=abs(n)
            while n >=-1:
                #print('outside')
                if int(n*3)!= n*3:
                    flag = 1
                    #print('inside')
                    break
        
                n = n * 3
            
            
        if flag == 1:
            #print ('false')
            return False
        elif flag == 0:
            #print('true')
            return True

A = Solution()
A.isPowerOfThree (-1/6)