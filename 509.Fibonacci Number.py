class Solution:
    def fib(self, N: int) -> int:
        
        l =[]
        l1 = 0
        l2 = 1
        
        l.append(l1)
        l.append(l2)
        
        
        for i in range (1,N-1):
            l3 = l[i]+l[i-1] 
            l.append(l3)
        
        #print (l)
        
        k = 0
        
        if N == 0:
            return (0)
        else:
        
            for j in range (N-2,N):
                k= k + l[j]
            
            
            return (k)
A = Solution()
A.fib(0)           