class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        l = 0
        r = 0

        for num in nums:
            r += num
            if l<num:
                l = num

        ans = float("inf")
        while l<=r:
            mid = (l+r)//2
            sumEle = 0
            count = 1
            
            for num in nums:
                if sumEle+num>mid:
                    count +=1
                    sumEle = num
                else:
                    sumEle += num
            if count<= m:
                ans = min(ans,mid)
                r = mid-1
            else:
                l=mid+1
        return ans
