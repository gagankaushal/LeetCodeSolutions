class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        Dict = dict(zip(nums, [0] * len(nums)))

        #print(Dict)

        for i in nums:
            Dict[i]=Dict[i] + 1

        #print(Dict)
        for i in Dict:
            if Dict[i] == 1:
                # print ('h')
                #Dict.append(Dict[i])
                #print(Dict[len(Dict)] - 1)
                return(i)
                break
                
        return (None)

        #print(Dict)



A=Solution()
#A.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
A.singleNonDuplicate([3,3,7,7,10,11,11])