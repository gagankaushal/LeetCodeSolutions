"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return head

        ptr = head
        
        while ptr:
            newNode = Node(ptr.val, ptr.next, None)
            # newNode.next = ptr.next
            ptr.next = newNode
            ptr = newNode.next
        
        
        ptr = head
        
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next
            
            
        ptrOld = head
        ptrNew = head.next
        headOld = head.next
        while ptrOld:
            
            ptrOld.next = ptrOld.next.next
            
            ptrOld = ptrOld.next
            ptrNew.next = ptrNew.next.next if ptrNew.next else None
            
            ptrNew = ptrNew.next
        
        return headOld
            
        
