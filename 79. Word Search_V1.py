class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        buffer = []

        for i in range (len(board)):
            for j in range (len(board[0])):

                buffer.append(board[i][j])

        count = 0

        for i in word:
            if i in buffer:
                count = count + 1
                buffer[buffer.index(i)] = 0

        if count == len(word):
   #         print ('True')
  #          print(buffer)
            return True

        else:
 #           print('False')
#            print(buffer)
            return False





