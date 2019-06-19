class Solution:
    def isHappy(self, n: int) -> bool:

        counter = 0
        while (n >= 0 and counter<1000 ):
            sum = 0
            # print(n)

            while (n > 0):
                newDigit = int(n % 10)
                n = int(n / 10)
                sum = sum + newDigit ** 2

            n = sum
            #print(n)
            counter = counter + 1

        if sum == 1:
            #print('True')
            return True
        else:
            #print('False')
            return False
