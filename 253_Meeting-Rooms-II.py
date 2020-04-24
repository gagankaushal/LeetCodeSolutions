class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        sort based on the start time
        
        add the ending time to min heap
        
        add remaining also
        - remove the meeting if new room's start time > end time of heap
        
        
        
        
        '''
        
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x[0])
        
        rooms = []
        
        heapq.heappush(rooms,intervals[0][1])
        
        for i in intervals[1:]:
            
            # remove
            if rooms[0]<= i[0]:
                heapq.heappop(rooms)
                
            heapq.heappush(rooms, i[1])
        
        return len(rooms)