# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None:
            return None
        current = headA
        d = {}
        while current is not None:
            d[current] = 1
            current = current.next
        #print(d)
        current = headB
        while current is not None:
            if current in d:
                return current
            current = current.next
        return None
