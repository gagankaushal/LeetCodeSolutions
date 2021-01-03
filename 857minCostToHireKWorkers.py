class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        
        
        # worker = sorted((w/q,q,w) for q, w in zip(quality, wage))
        # print(worker)
        
        # sort based on the ratio...this would help in having the max ratio at the end 
        workers = []
        for q, w in zip(quality, wage):
            workers.append((w/q,q,w))
        
        workers.sort(key = lambda x: x[0])
        print(workers)
        qualityHeap = []
        qualitySum = 0
        ans = float("inf")
        for ratio, q, w in workers:
            heappush(qualityHeap, -q)
            qualitySum += q
            
            if len(qualityHeap)>K:
                qualitySum += heappop(qualityHeap)
                # after removing again calculate the ratio
            if len(qualityHeap)==K:
                ans = min(ans, ratio*qualitySum)
        return ans
    
