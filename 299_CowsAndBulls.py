class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        '''
        fiding bulls - take 2 pointers..if same then incfrment counter
        
        finding cows - store all digits if not equal(bcoz bull) and letter in secret...
        for each of these, I'll update the number to x or something to mark it has been visited...handle the duplicate number
        '''
        
#         secretPointer = 0
#         guessPointer = 0
        
#         bulls = 0
#         cows = 0
        
#         # visited = [0]*len(secret)
#         visitedSecret = Counter(secret)
        
#         print (visitedSecret)
#         # return True
        
#         while secretPointer < len(secret) and guessPointer < len(guess):
#             if secret[secretPointer]    ==  guess[guessPointer]:
#                 bulls += 1
# #                 # secret[secretPointer] = 'V'
# #                 visited[secretPointer] = 1
#                 visitedSecret[secret[secretPointer] ] -= 1
#             else:
# #                 for i in range(len(secret)):
#                 if secret[secretPointer] in visitedSecret and visitedSecret[secret[secretPointer] ]!=0:
#                     cows+=1
#                     visitedSecret[secret[secretPointer] ] -= 1
            
#                     # if guess[guessPointer]==secret[i]  and visited[i]==0 :
# #                         cows += 1
# #                         visited[i] = 1
#             secretPointer += 1
#             guessPointer += 1
#         return str(bulls)+'A'+str(cows)+'B'

        visited = defaultdict(int)
        
        secretPointer = 0
        guessPointer = 0
        
        cows = 0
        bulls = 0
        
        while secretPointer < len(secret):
            
            if guess[guessPointer] == secret[secretPointer]:
                bulls += 1
            
            else:
                #if already less for which we are ready to suppy, then bull
                # or if guess letter is already pretn,..becasue in past the letter was supplied by secret word
                cows +=  int(visited[secret[secretPointer]]<0) + int(visited[guess[guessPointer]]>0)
                # make a particular available, so +1
                visited[secret[secretPointer]]+= 1
                # guess has consumed the letter...so net would b
                visited[guess[guessPointer]] -= 1
            secretPointer += 1
            guessPointer += 1

        return "{}A{}B".format(bulls, cows)
