# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def invert(root):
            if not root:
                return 
            
            l = root.left
            r = root.right
            
            if (not l and not r):
                return
            
            root.right = l
            root.left = r
            
            invert(root.left)
            invert(root.right)
        
        invert(root)
        return root
