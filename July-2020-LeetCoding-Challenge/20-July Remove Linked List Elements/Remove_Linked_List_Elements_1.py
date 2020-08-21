# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head==None:
            return head
        if head.next==None:
            if head.val == val:
                head = None
            return head
        
        prev=None
        curr = head
        while(curr!=None):
            if curr.val==val:
                temp = curr.next
                if prev!=None:
                    prev.next = temp
                    curr = curr.next
                else:
                    head = curr.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next
                
        return head
