class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # for col in range(row+1,len(matrix[0]) ):
        #     for row in range(len(matrix)):
        for col in range(len(matrix[0]) ):
            for row in range(col+1,len(matrix)):
          
                
                # transpose
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        print(matrix)
        for row in range(len(matrix)):
            start = 0
            end = len(matrix[0])-1
            while start < end:
                matrix[row][start], matrix[row][end] = matrix[row][end], matrix[row][start] 
                start += 1
                end -= 1
        
        # matrix[row][col], matrix[row][len(matrix)-col-1] = matrix[col][row], matrix[row][col]
        
        # invert rows
        # for row in range(len(matrix)):
        
            
                
        
        
