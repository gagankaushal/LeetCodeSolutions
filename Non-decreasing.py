class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        flagMountain = 0
        flagValley = 0

        for i in range(0, len(nums)-1):

            if i <= len(nums)-3:
                if nums[i] < nums[i + 1] > nums[i + 2]:# and i+2 <=  len(nums)-1:
                    flagMountain = flagMountain + 1
                elif nums[i] > nums[i + 1] < nums[i + 2]:
                    flagValley = flagValley + 1

            elif i > len(nums)-3:
                if nums[i] < nums[i + 1] :# and i+2 <=  len(nums)-1:

                    flagMountain = flagMountain + 1
                elif nums[i] > nums[i + 1]:
                    #if nums[i - 1] < nums[i + 1]:
                        flagValley = flagValley + 1




        print(flagMountain,flagValley)

        if flagMountain == 0 or flagValley == 0 or flagMountain >1 or flagValley >1:
            print('False')

            return False
        elif flagMountain == 1 or flagValley == 1:
            print('True')
            return True

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            
            ret = Solution().checkPossibility(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()