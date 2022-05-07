"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        
        arr = []
    
        def helper(root, arr):
            if not root:
                return arr
            arr.append(root.val)
            for i in root.children:
                helper(i, arr)
    
        helper(root, arr)  
        return arr
