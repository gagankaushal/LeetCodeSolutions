class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    
    # for each element, check the previous diagonal element (if exists)
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-1>= 0 and c-1>=0 and matrix[r-1][c-1] !=val:
                    return False
        return True
