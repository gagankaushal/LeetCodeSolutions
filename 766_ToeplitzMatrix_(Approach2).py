class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    
    # go from bottm to top, then left to right
        # go from bottom to top
        
        # col = 0
        
        for row in range(1,len(matrix)-1):
            col = 0
            
            baseValue = matrix[row][col]
            col += 1
            row += 1
            while col <= len(matrix[0])-1 and row <= len(matrix)-1:
                

                if baseValue != matrix[row][col]:
                    return False
                col += 1
                row += 1
        # go from left to right
        
        # row = 0
        
        for col in range(len(matrix[0])-1):
            row = 0
            print(matrix[row][col])
            baseValue = matrix[row][col]
            col += 1
            row += 1
            
            while col <= len(matrix[0])-1 and row <= len(matrix)-1:
               
                if baseValue != matrix[row][col]:
                    return False
                col += 1
                row += 1

        return True
        
            
        
        
