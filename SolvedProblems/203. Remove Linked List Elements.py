# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next 
            
        ptr = head
        
        while ptr:
            while ptr.next and ptr.next.val==val:
                ptr.next = ptr.next.next
            ptr = ptr.next    
        
        return head 
