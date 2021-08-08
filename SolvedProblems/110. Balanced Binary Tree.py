# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def balance(self, root, height):
        if not root:
            return height, True 
        left, l_balanced = self.balance(root.left, height+1)
        right, r_balanced = self.balance(root.right, height+1)
        
        if abs(left-right)<=1 and l_balanced and r_balanced:
            return max(left, right), True
        
        return 0, False
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.balance(root, 0)[1]        
    
