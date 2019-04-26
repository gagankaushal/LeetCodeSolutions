class Solution:
    def intersection(self, nums1, nums2) -> int:
        
        finalList = []
        finalest = {}
        ListWithoutRepetition = []
        
        for i in nums1:
            for j in nums2:         
                if i == j :
                    finalList.append(i)
        
        finalest = dict.fromkeys(finalList,0)
        
	for k in finalList:
            if k in finalList:
                finalest[k] =finalest[k] + 1
        
        for i in finalest.keys():
            ListWithoutRepetition.append(i)
        
        return (ListWithoutRepetition)
        
A = Solution()
A.intersection([4,9,5], [9,4,9,8,4])
                    