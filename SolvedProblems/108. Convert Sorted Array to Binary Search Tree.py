# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums is None:
            return None
       
        def weird(nums):
            if len(nums)==0:
                return           
            mid = len(nums)//2
            node = TreeNode()
            node.val = nums[mid]
            node.left = weird(nums[:mid])
            node.right = weird(nums[mid+1:])
            return node
          
        x = weird(nums)
        return x 
