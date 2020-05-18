# Heap is really a good data structure to use when we want to pick the top k largest numbers from a list. 
# This is because the heap property always keeps the top element as either min or max
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Heapify -> Time Complexity: O(n)
        # Heappop -> Time Complexity: O(log n)
        # Heappush -> Time Complexity: O(log n)
        
        # heapify creates a min-heap by default. So, convert it into max-heap by multiplying to -1
        # Priority queue is same as heap
        for i in range(len(stones)):
            stones[i] *= -1
            
        heapq.heapify(stones)
        
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            
            if (stone1 != stone2):
                heapq.heappush(stones, stone1 - stone2)
        
        if len(stones)>0:
            return -heapq.heappop(stones)
        else:
            return 0
            
            
            
        
