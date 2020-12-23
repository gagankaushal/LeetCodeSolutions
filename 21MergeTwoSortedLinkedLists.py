# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
#         if not l1:
#             return l2
#         elif not l2:
#             return l1
        
        output = ListNode(0)
        
        curr = output
        
        while l1 and l2:
            if l1.val <= l2.val:
                # curr.next = ListNode(l1.val)
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = ListNode(l2.val)
                l2 = l2.next
            curr = curr.next
        
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        return output.next
            
            
            
        
        
        
