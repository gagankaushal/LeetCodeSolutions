class Solution:
    def removeOuterParentheses(self, S) -> str:
        #(()())(())(()(()))
        #()()(())()(())

        startBraces = []
        endBraces = []
        ActualendBraces = []
        ActualstartBraces = []


        for i in S:
            if i == '(':
                startBraces.append(i)
                ActualstartBraces.append(i)
            elif i ==')':
                endBraces.append(i)
                ActualendBraces.append(i)

        print (startBraces)
        print(endBraces)



        startBraces = []
        endBraces= []

        for i in range(0,len(S)):
            if S[i] == '(':
                startBraces.append(i)
            elif S[i] ==')':
                endBraces.append(i)

        print (startBraces)
        print(endBraces)
        LastNoneIndex = len(startBraces)-1




        for i in range(len(endBraces) - 1, 0, -1):

           if i == len(endBraces) - 1:
               if endBraces[i]  == endBraces[i-1] + 1:
                    endBraces[i] = None
           else:
               if endBraces[i]  == endBraces[i-1] + 1 and endBraces[i+1] != None :
                    endBraces[i] = None

        #print (len(startBraces))
        for i in range(0, len(startBraces)-1):
            #print(i)
            if i==0:
                if startBraces[i] + 1 == startBraces[i + 1]:
                    startBraces[i] = None
                    LastNoneIndex = i


            else:

               print ('o')


               if startBraces[i] + 1 == startBraces[i+1]:
                   for j in range (LastNoneIndex+1,i+1):
                       print (endBraces[j])
                       if endBraces[j]==None:
                            #print('oye')
                            startBraces[i] = None
                            LastNoneIndex = i






        print(startBraces)
        print(endBraces)

A = Solution()
A.removeOuterParentheses('(()())(())(()(()))')
#A.removeOuterParentheses('(()())(())')
#()()





