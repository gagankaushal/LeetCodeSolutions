class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        RealA = ''
        RealB = ''
        ImgA = ''
        ImgB = ''

        for i in range(0, len(a)):
            if a[i] == '+':
                indexOfA = i
                break
            else:
                RealA = RealA + a[i]

        for i in range(indexOfA + 1, len(a)-1):
            ImgA = ImgA + a[i]

        for i in range(0, len(b)):
            if b[i] == '+':
                indexOfB = i
                break
            else:
                RealB = RealB + b[i]

        for i in range(indexOfB + 1, len(b)-1):
            ImgB = ImgB + b[i]

        #print(RealA, ImgA)

        #print(RealB, ImgB)

        Im1stTerm = int(RealA)*int(ImgB)
        Im2ndTerm = int(RealB)*int(ImgA)
        Re3rdTerm = int(RealA) * int(RealB)
        Re4thTerm = -(int(ImgA) * int(ImgB))

        Im = Im1stTerm + Im2ndTerm
        Re = Re3rdTerm + Re4thTerm

        #print(str(Re) + '+' + str(Im) + 'i' )

        return(str(Re) + '+' + str(Im) + 'i')
