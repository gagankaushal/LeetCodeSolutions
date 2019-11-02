class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """


        row = len(board)
        column = len(board[0])


        copy = [[board[ro][col] for col in range(column)] for ro in range(row)]



        neighbours = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        for r in range(row):
            for c in range(column):

                sumOfNeighbours = 0

                for n in neighbours:
                    rowOfNeighbour = r + n[0]
                    columnOfNeighbour = c + n[1]

                    if (0 <= rowOfNeighbour < row) and ( 0 <= columnOfNeighbour < column ) and (copy[rowOfNeighbour][columnOfNeighbour] == 1):
                        sumOfNeighbours += 1

                if (copy[r][c] == 1) and (sumOfNeighbours < 2 or sumOfNeighbours > 3):
                    board [r][c] = 0

                elif (copy[r][c] == 0) and sumOfNeighbours == 3:
                    board [r][c] = 1

        