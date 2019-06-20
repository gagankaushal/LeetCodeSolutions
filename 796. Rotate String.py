class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        b = list(B)
        a = list(A)

        if len(A) == 0:
            if len(B) == 0:
                return True
            else:
                return False
        else:

            for i in range(0, len(a)):
                for j in range(0, len(b)):
                    if a[i] == b[j]:
                        if j+1 <= len(b)-1:
                            if a[i+1]==b[j+1]:
                                indexA = i
                                print(a[i], b[j])
                                indexB = j
                                break
                        else:
                                indexA = i
                                print(a[i], b[j])
                                indexB = j
                                break
                else:
                    continue
                break

            toMove = indexA - indexB
            temp = ''
            print(toMove, i, j)
            if toMove > 0:  # right shift B
                while (toMove > 0):

                    temp = b[len(b) - 1]
                    for i in range(len(b) - 2, -1, -1):
                        b[i + 1] = b[i]
                    b[0] = temp
                    toMove = toMove - 1
                if (b == a):
                    return True
                else:
                    print(str(b), a)
                    return False

            else:  # right shift the A

                if a[0] == a[len(a) - 1]:

                    toMove = toMove - 1
                while (toMove < 0):

                        temp = a[len(A) - 1]
                        for i in range(len(a) - 2, -1, -1):
                            a[i + 1] = a[i]
                        a[0] = temp

                        toMove = toMove + 1

                if (a == b):
                    print(a, b)
                    return True
                else:
                    print(a, b)
                    return False


c=Solution()
#c.rotateString("bbbacddceeb","ceebbbbacdd")
#c.rotateString("abcde","cdeab")
c.rotateString("slqhrmnxqjtyzvfldllvixbzpswspednzonqkjrlaltguusdxvknoasahjgqdquinucpmlxtdzpnmvxqtfwm"
               "xdqozgmaaycjebjs",
               "llvixbzpswspednzonqkjrlaltguusdxvknoasahjgqdquinucpmlxtdzpnmvxqtfwmxdqozgmaaycjebjss"
               "lqhrmnxqjtyzvfld")