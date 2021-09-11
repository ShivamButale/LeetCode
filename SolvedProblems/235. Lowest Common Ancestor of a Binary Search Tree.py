# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def starter(root):
            init = root
         
            if p.val < root.val:
                l1 = root.left 
            elif p.val > root.val:
                l1 = root.right
            else:
                l1 = root
        
            if q.val < root.val:
                l2 = root.left 
            elif q.val > root.val:
                l2 = root.right
            else:
                l2 = root
           
            
            if l1!=l2:
                return init
            else:   
                return starter(l1)
            
        return starter(root)
     
