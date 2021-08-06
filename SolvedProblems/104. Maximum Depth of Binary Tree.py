# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        val = 0      
        def depth(root, val):
            if root is None:
                return 0
            else:
                 return 1 + max(depth(root.left, val), depth(root.right, val))

        return depth(root, val)
           
