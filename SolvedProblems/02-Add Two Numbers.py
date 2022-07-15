# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = []
        a1 = l1
        while(a1):
            n1.append(a1.val)
            a1 = a1.next
        
        n2 = []
        a2 = l2
        while(a2):
            n2.append(a2.val)
            a2 = a2.next
        
        n1.reverse()
        n2.reverse()
       
        num1 = ""
        for i in n1:
            num1 += str(i)
        num1 = int(num1)
        
        num2 = ""
        for i in n2:
            num2 += str(i)
        num2 = int(num2)
        
        final = num1 + num2 
        s_final_reverse = str(final)[::-1]

        i = 0
        root = ListNode()
        abc = root
        root.val = s_final_reverse[i]
        i += 1
        
        while(i < len(s_final_reverse)):
            f1 = ListNode()
            f1.val = s_final_reverse[i]
            i = i + 1
            root.next = f1
            root = f1

        return abc
