class Solution:
    def myPow(self, x: float, n: int) -> float:
        # def P (x,n)->float:
        ans = 1
        temp = 1

        if n > 0:
            if x < 1:
                if n % 2 == 1:
                    temp = x
                    while (n % 2 == 1):
                        x = x * x
                        n = int(n / 2)
                while (n > 0):
                    ans = ans * x
                    n = n - 1
                return ans * temp
            else:
                while (n > 0):
                    ans = ans * x
                    n = n - 1
                return ans
        elif n == 0:
            return 1
        else:
            while (n < 0):
                ans = ans / x
                n = n + 1
            return ans


