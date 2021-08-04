# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
        
        # If both have left
        if p.left and q.left:
            x = self.isSameTree(p.left, q.left)
            if x==False:
                return False
        else:
            # If only one has left
            if p.left or q.left:
                return False
        #if both dont have left
        #Do nothing
        
        # If both have right
        if p.right and q.right:
            x = self.isSameTree(p.right, q.right)
            if x == False:
                return False
        else:
            # If only one has left
            if p.right or q.right:
                return False
        #if both dont have right
        #Do nothing
        
        return True
