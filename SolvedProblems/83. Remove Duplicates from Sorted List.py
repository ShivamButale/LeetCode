# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        if head is None or head.next==None:
            return head
        
        # Iterate through the linked list
        i = head
        
        while(i.next):
            temp = i.next
            if temp.val == i.val:
                i.next = temp.next 
            else:
                i = i.next
                
        return head
