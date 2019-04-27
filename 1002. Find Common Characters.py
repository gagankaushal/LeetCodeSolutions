class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        l = []
        k = []

        for u in A[0]:
            l.append(u)
        
        for i in range(1,len(A)):  #main strings that need to be compared are present in A
            y = list (A[i])  
            for j in range(0,len(l)): # to pick individual characters of main string (0e.g. elements of A[0]..eventually it contains the common elements of A[0] and A[1]
                 
                for r in range (0,len(y)): # to iterate over charactes of main string (next elements)
                    if l[j] == y[r]:
                        k.append(l[j])
                        
                        y[r]=''
                        
                        break
            l = k
            k =[]
                
        return (l)
    
A = Solution()
A.commonChars(["bella","label","roller"])