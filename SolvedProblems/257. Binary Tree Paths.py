# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        l = []
        def dfs(root, curr):
            if root.left is None and root.right is None:
                l.append(curr)
                return 
            if root.left:
                dfs(root.left, curr + '->' + str(root.left.val))
            if root.right:
                dfs(root.right, curr + '->' + str(root.right.val))
            return 
            
        dfs(root, str(root.val))
        return l
