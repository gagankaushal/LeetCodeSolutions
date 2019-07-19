class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        5 - 1
        5 + 1, 1, 1

        10 + 1, 1, 1

        integ = [1,5,10,50,100,500,1000]
        roms = ['I','V','X','L','C','D','M']

        listOfmappings = dict (zip(integ,roms))
        print(listOfmappings)
        answer = []

        if num in listOfmappings:
            return(listOfmappings[num])

        else:
            for i in range(1,4):
                if num-i in listOfmappings:
                    answer.append(listOfmappings[num-i])
                    while(i>0):
                        answer.append(listOfmappings[1])
                        i = i-1
                    #ANS = str(answer)
                    print(''.join(answer))
                    break

A = Solution()
A.intToRoman()