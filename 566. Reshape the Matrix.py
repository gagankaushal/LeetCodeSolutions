class Solution:
    def matrixReshape(self, nums, r: int, c: int) -> int:

        # find the number of rows and coulmns of a matrix

        numberOfRows = len(nums)
        numberOfColumns = len(nums[0])



        if (numberOfRows * numberOfColumns == r * c):
            # prod of this == r*c:
            #then
            #possible
            #reshapedMatrix = [r][c]
            reshapedMatrix = [[0 for x in range(c)] for y in range(r)]

            buffermatrix = []

            for i in range(0, numberOfRows):  # 1
                for j in range(0, numberOfColumns):  # 4
                    buffermatrix.append(nums[i][j])

            k = 0

            for i in range(0, r):  # 1
                for j in range(0, c):  # 4
                    reshapedMatrix[i][j] = buffermatrix[k] #.append(nums[i][j])
                    k= k+1


            #print (buffermatrix,reshapedMatrix)
            #initialize a matrix with r and c and then input all the elements one by one
	    return (reshapedMatrix)
		
        else:
            return (nums)





A=Solution()
A.matrixReshape([[1,2,3],[4,5,6]],3,2)