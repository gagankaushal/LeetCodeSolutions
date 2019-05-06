class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        flag = 0

        if n != 0 and n > 0:

            while n > 1:
                if n % 2 != 0:
                    flag = 1
                    break

                n = n / 2

        elif n == 0:
            flag = 1

        elif -1 >= n:
            flag = 1

        elif -1 < n < 0:
            # n=abs(n)
            while n >= -1:
                # print('outside')
                if int(n * 2) != n * 2:
                    flag = 1
                    # print('inside')
                    break

                n = n * 2

        if flag == 1:
            #print('false')
            return False
        elif flag == 0:
            #print('true')
            return True

A = Solution()
A.isPowerOfTwo(-1)
