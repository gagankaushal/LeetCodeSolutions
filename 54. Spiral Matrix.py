class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
 
        minM = 0
        minN = 0
        maxM = len(matrix)
        
        #numberOfElements
        count = 0
        arr = []
        # for i in range(maxM):
        
        if matrix == []:
            return (arr)
        
        else:
            maxN = len(matrix[0])
            numberOfElements = maxM* maxN
            
       
            while (count <numberOfElements):
                #   m = min n = 0,1,2,...max
                for j in range(minN,maxN):
                    arr.append(matrix[minM][j])
                    count = count + 1
                minM = minM + 1
                #           print(arr)

                if (count==numberOfElements):
                    return (arr)
                    break

                # n = max m = 1,2,3, max
                for i in range(minM, maxM):
                    arr.append(matrix[i][maxN-1])
                    count = count + 1
                maxN = maxN - 1
                #   print(arr)
                #count = count + 1

                if (count==numberOfElements):
                    return (arr)
                    break

                # m = max n = max-1,max-2,.....0
                for j in range(maxN-1, minN-1, -1):
                    arr.append(matrix[maxM-1][j])
                    count = count + 1
                maxM = maxM - 1
                #          print(arr)
                #ount = count + 1


                if (count==numberOfElements):
                    return (arr)
                    break

                # n = min m = max-1......
                for i in range(maxM-1, minM-1, -1):
                    arr.append(matrix[i][minN])
                    count = count + 1
                minN = minN + 1


                if (count==numberOfElements):
                    return (arr)
                    break


                #count = count + 1



A = Solution()
A.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])