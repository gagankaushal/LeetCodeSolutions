class Solution:
    def convert(self, s: str, numRows: int) -> str:
        Matrix = [['0' for x in range(len(s))] for y in range(numRows)]

        j = 0
        stringIndex = 0
        count = 0
        while (count < len(s)):
            for i in range(0, numRows):
                #print (stringIndex+1,len(s))
                try:

                    Matrix[i][j] = s[stringIndex]
                    stringIndex += 1
                    count += 1
                except IndexError:
                    break



            j += 1
            #stringIndex += 1

            if numRows==1:
                try:
                    Matrix[0][j] = s[stringIndex]
                    stringIndex += 1
                    count+=1
                    j += 1
                except IndexError:
                    break
            else:

                for i in range(numRows-2,0,-1):
                    try:
                        Matrix[i][j] = s[stringIndex]
                        stringIndex += 1
                        j += 1
                        count += 1
                    except IndexError:
                        break



            #print (j)
        '''
        for m in Matrix:

            print (m)
        print('------------------------')
        '''
        final = []

        for y in Matrix:
            for t in y:
                if t != '0':
                    final.append(t)

        return (''.join(final))
