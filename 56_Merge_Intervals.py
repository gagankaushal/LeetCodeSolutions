class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        # sort
        # compare the end and start...append
        
        if len(intervals)<2:
            return intervals
        newInterval = []
        intervals.sort(key = lambda x: x[0])
        
        index = 0
        # for index in range(len(intervals)):
        while index< len(intervals)-1:
            if (intervals[index][1]> intervals[index][0]):
                newInterval.append([intervals[index][0],intervals[index+1][1]])
                index += 1
            else:
                newInterval.append([interval[index]])
        print(newInterval)
        return newInterval
        '''
        
        intervals.sort(key = lambda x: x[0])
        merged = []
        
        for interval in intervals:
            
            if not merged or (merged[-1][1]< interval[0]):
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged
