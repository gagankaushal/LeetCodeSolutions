# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        nodes = []
        
        head = point = ListNode(0)
        
        for l in lists:
            
            while l:
                nodes.append(l.val)
                l = l.next
        
        
        for i in sorted(nodes):
            #print(i)
            point.next = ListNode(i)
            point = point.next
        return (head.next)
            
            
        