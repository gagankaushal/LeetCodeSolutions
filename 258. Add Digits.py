class Solution:
    def addDigits(self, num: int) -> int:

        #print(num)
        stI = str(num)
        sum = 10

        #print(num)
        while (len(str(sum)) > 1):
            sum = 0
            #print(num,sum)
            while (num>=1):
                newDigit = int(num % 10)
                #print(num)
                num = int(num / 10)
                #print (num)
                sum = sum + newDigit
                #print (sum, num, newDigit)
            #print(sum)

            lenSum = len(str(sum))

            if lenSum == 1:
                #print(sum)
                return sum
            else:
                num = sum