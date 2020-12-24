class Solution:
    
    WHITE = 1
    GRAY = 2
    BLACK = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adjList = defaultdict(list)
        
        # create adj list - source:[destination nodes]
        for dest, src in prerequisites:
            adjList[src].append(dest)
        print(adjList)
        
        # tracker
        color = {k: Solution.WHITE for k in range(numCourses)}
        
        isPossible = True    
        topologicalSortedOrder = []
        # dfs
        def dfs(node):
            nonlocal isPossible
            # nonlocal topologicalSortedOrder
            # print(topologicalSortedOrder)
            
            
            # don't recurse if cycle found
            
            if not isPossible:
                return
            
            color[node] = Solution.GRAY
            
            if node in adjList:
                for neighbour in adjList[node]:
                    # do dfs on neighbour if not visited
                    if color[neighbour] == Solution.WHITE:
                        dfs(neighbour)
                        
                        # cycle exists
                    elif color[neighbour] == Solution.GRAY:
                        isPossible = False
            
            
            color[node] = Solution.BLACK
            topologicalSortedOrder.append(node)
        
        
        
        
        
        
        for vertex in range(numCourses):    
            if color[vertex] == Solution.WHITE:
                dfs(vertex)
                
                
        
        return topologicalSortedOrder[::-1] if isPossible else []
        
            
