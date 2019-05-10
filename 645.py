class Solution:
    def findErrorNums(self, nums) -> int:
        nums.sort()
        dic = {}
        finalAns = []

        dic = dict.fromkeys(nums,0)
        print(dic)
        for i in nums:
            dic[i] = dic[i]+ 1
            if dic[i]==2:
                indexOfDoubleNumber = i

        print(dic)

        for i in dic:

            if dic[i] == 2:
                finalAns.append(i)
                break

        if nums[0]!=1:

            finalAns.append(1)
        else:
            if i == len(nums):
                finalAns.append(i-1)
            elif i +1 == len(nums):
                finalAns.append(i+1)
            else:
                upper = i+1
                lower = i-1
                if upper in dict.keys():
                    finalAns.append(i - 1)
                elif lower in dict:
                    finalAns.append(i + 1)

        print (finalAns)
        return (finalAns)



A=Solution()
A.findErrorNums([8,7,3,5,3,6,1,4])