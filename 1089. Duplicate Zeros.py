class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        j = 0
        count = 0
        listOfIndexZeroes = []
        
        originalLength = len(arr)
        for i in arr:
           # print (i)
            if i == 0:
                count = count + 1
                #print(i, j)
                listOfIndexZeroes.append(arr.index(i,j))
                #print(arr.index(i,2))
                j = arr.index(i,j)+1

        #print (listOfIndexZeroes)

        listOfIndexZeroes.sort(reverse= True)
        for i in listOfIndexZeroes:

            arr.insert(i,0)

        #print (arr[1:originalLength])
        #return(arr)
        #str(arr)
        #arr[1:originalLength]
        #arr=list(arr)
        
        for i in range(len(arr)-1,originalLength-1,-1):
            arr.pop()

        if count ==0:
            return None


A=Solution()
A.duplicateZeros([1,0,2,3,0,4,5,0])
#A.duplicateZeros([1,2,3])

