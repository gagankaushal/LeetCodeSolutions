class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:


        def newDiv(x,y):
            return 10000000 if y ==0 else x/y


        if (points[1][1] == points[0][1] and  points[1][0] == points[0][0] or points[2][1] == points[1][1] and points[2][0] == points[1][0] or points[2][1] == points[0][1] and points[2][0] == points[0][0]):

                 #  print('F')
                   return False
       
        else:

            slope1 = newDiv(points[1][1] - points[0][1], points[1][0] - points[0][0])

            slope2 = newDiv(points[2][1] - points[1][1], points[2][0] - points[1][0])

            if slope1 == slope2:
                #print('F')
                return False
            else:
                #print('T')
                return True

A = Solution()
A.isBoomerang([[0,0],[1,1],[1,1]])