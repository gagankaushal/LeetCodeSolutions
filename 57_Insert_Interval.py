class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        merged = []
        
        # add all elements before newInterval
        
        # add/merge newInterval
        
        # add ele after newInterval and merge if required
        
        
        idx = 0
        n = len(intervals)
        
        while idx<n and intervals[idx][0] < newInterval[0]:
            merged.append(intervals[idx])
            idx += 1
        
        
        if not merged or merged[-1][1] < newInterval[0]:
            merged.append(newInterval)
        else:
            merged[-1][1] = max(merged[-1][1], newInterval[1])
            
        while idx<n:
            if merged[-1][1] < intervals[idx][0]:
                merged.append(intervals[idx])
            else:
                merged[-1][1] = max(merged[-1][1], intervals[idx][1])
            idx+= 1
        
        return merged
