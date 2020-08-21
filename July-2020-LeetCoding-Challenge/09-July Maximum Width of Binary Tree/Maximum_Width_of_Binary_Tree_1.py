# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        level = [(root, 0)]
        sol = 1
        
        while level:
            next_level = []
            sol = max(sol, level[-1][-1] - level[0][1] + 1)
            for node, pos in level:
                if node.left:
                    next_level.append((node.left, 2*pos))
                if node.right:
                    next_level.append((node.right, 2*pos+1))
            level = next_level
        
        return sol
