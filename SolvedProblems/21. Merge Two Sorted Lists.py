# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1==None:
            return l2 
        if l2==None:
            return l1
        
        p = ListNode()
        l3 = ListNode()
        l3 = p
        
        while(l1 and l2):
            if(l1.val == l2.val):
                print("******** CASE 1")
                p.val = l1.val
                print("**l3 = ", l3)
                p.next = ListNode()
                p = p.next
                p.val = l2.val
                print("**l3 = ", l3)
                l1 = l1.next
                l2 = l2.next
                if(l1 or l2):
                    p.next = ListNode()
                    p = p.next
            elif l1.val < l2.val:
                print("******** CASE 2")
                p.val = l1.val
                l1 = l1.next
                if(l1 or l2):
                    p.next = ListNode()
                    p = p.next
            else:
                print("******** CASE 3")
                p.val = l2.val
                l2 = l2.next
                if(l1 or l2):
                    p.next = ListNode()
                    p = p.next
        
        #If both over, remove extra 
        
        #If l1 remaining, append all remaining of l1 
        while(l1):
            p.val = l1.val
            l1 = l1.next
            if(l1): 
                p.next = ListNode()
                p = p.next
        
        #If l2 remaining, append all remaining of l2 
        while(l2):
            p.val = l2.val
            l2 = l2.next
            if(l2):
                p.next = ListNode()
                p = p.next
        
        print(l3)
        return l3
