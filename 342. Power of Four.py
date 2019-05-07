class Solution:
    def isPowerOfFour(self, num: int) -> bool:

        flag = 0

        if num != 0 and num > 0:

            while num > 1:
                if num % 4 != 0:
                    flag = 1
                    break

                num = num / 4

        elif num == 0:
            flag = 1

        elif -1 >= num:
            flag = 1

        elif -1 < num < 0:
            # n=abs(n)
            while num >= -1:
                # print('outside')
                if int(num * 4) != num * 4:
                    flag = 1
                    # print('inside')
                    break

                num = num * 4

        if flag == 1:
            #print('false')
            return False
        elif flag == 0:
            #print('true')
            return True



A = Solution()
A.isPowerOfFour(10)
