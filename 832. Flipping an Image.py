class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        for i in A:
            lengthOfInternalList = len(i)

        for i in range(0,len(A)): #Flip Horizontally
                
                for k in range (0,int(lengthOfInternalList/2)):

                    A[i][k] ,A[i][lengthOfInternalList-k-1] = A[i][lengthOfInternalList-k-1], A[i][k]
                    #print (i,A[i][k],A[i][lengthOfInternalList-k-1])

        #print (A)

        for i in range(0,len(A)):

            for j in range(0,len(A)): #invert an image
                if A[i][j] == 1:
                    A[i][j] = 0

                else:
                    A[i][j] = 1

        print (A)


B = Solution()
#B.flipAndInvertImage([[0,1,1],[1,0,1],[0,0,0]])
B.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
#B.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])