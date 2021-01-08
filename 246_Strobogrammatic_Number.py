class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        # stroboNumbers = defaultdict(str)
        # stroboNumbers = {'6':'9', '9':'6', '1':'1', '8':'8','0':'0', '2':None, '3':None, '4':None, '5':None, '7': None}
        stroboNumbers = {'6':'9', '9':'6', '1':'1', '8':'8','0':'0'}
        print(stroboNumbers.get('5'))
        # stroboNumbers[6] = 9
        left = 0
        right = len(num)-1
        while left <= right:
            if stroboNumbers.get(num[left]) != num[right]:
                return False
            left += 1
            right -= 1
        return True
