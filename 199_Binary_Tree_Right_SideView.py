# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        output = []
        
        if not root:
            return []
        
        def dfs(node, level):        
            if level == len(output):
                output.append(node.val)
                
            for child in [node.right, node.left]:
                if child:
                    dfs(child, level +1 )
                    
        dfs(root,0)
        return output
            
            
        
