class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        B = []
        countLeft = 0
        countRight = 0

        if len(A) < 3:
            return False

        elif len(A) >= 3:

            for i in A:
                B.append(i)

            B.sort()

            for j in range(0, len(A)):

                if B[len(B) - 1] == A[j]:
                    middleIndex = j
                    break

            if A[middleIndex] == A[0] or A[middleIndex] == A[len(A) - 1]:
                return False

            else:
                for k in range(0, middleIndex):
                    if (A[k] >= A[k + 1]):
                        countLeft =  1
                        break

                if countLeft == 1:
                    return False

                for k in range(middleIndex, len(A) - 1):
                    if (A[k] <= A[k + 1]):
                        countRight =  1
                        break
                if countRight ==1:
                    return False

                elif countLeft == 0 and countRight == 0:
                    return True

C = Solution()
C.validMountainArray([0,1,2,3,4,5,6,7,9,8])


