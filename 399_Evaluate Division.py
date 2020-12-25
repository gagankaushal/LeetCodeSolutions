class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(dict)
        
        # create graph
        for (x,y), value in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1.0/value
            
            
        # dfs
        def dfs(x,y,visited):
            
            if x not in graph or y not in graph:
                return -1.0
            
            if y in graph[x]:
                return graph[x][y]
            
            for i in graph[x]:
                # x/y....x/i *  i/y
                if i not in visited:
                    
                    visited.add(i)
                    temp = dfs(i,y,visited)
                    # print(graph)
                    if temp == -1.0:
                        continue
                    else:
                        return graph[x][i]*temp
            return -1.0
                
        
        res = []
        
        for query in queries:
            res.append(dfs(query[0], query[1], set()))
        return res
    
    
