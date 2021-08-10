# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        curr_sum = 0
       
        
        def findSum(root: TreeNode, curr_sum: int):
            l = 0
            r = 0
            curr_sum += root.val 
            if not root.left and not root.right and curr_sum == targetSum:
                return True 
            #If left child present
            if root.left:
                l = findSum(root.left, curr_sum)
                if l== True:
                    return True
            #If right child present 
            if root.right:
                r = findSum(root.right, curr_sum)
                if r==True:
                    return True
        
        if root:
            return findSum(root, 0)
        else:
            return False
