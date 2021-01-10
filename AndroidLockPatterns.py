class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        
        def backtrack(curr, visited):
            if len(visited)>=m:
                self.count += 1
            if len(visited)==n:
                return
            for next in range(1,10):
                if next in visited:
                    continue
                edge = (min(curr, next), max(curr, next))
                if edge not in skip or skip[edge] in visited:
                    visited.add(next)
                    backtrack(next,visited)
                    visited.remove(next)
            
        skip = {
            (1,3):2,
            (1,7):4,
            (1,9):5,
            (2,8):5,
            (3,7):5,
            (3,9):6,
            (4,6):5,
            (7,9):8
        }
        
        self.count = 0
        
        for point in range(1,10):
            backtrack(point, set([point]))
        
        return self.count 
