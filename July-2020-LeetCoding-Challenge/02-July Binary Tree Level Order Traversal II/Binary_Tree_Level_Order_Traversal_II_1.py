# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        l1 = []
        l2 = []
        if root:
            q = []
            q.append(root)
            while(len(q)>0):
                levelSize = len(q)
                l1 = []
                while levelSize:
                    l1.append(q[0].val)
                    node = q.pop(0)
                    if node.left is not None:
                        q.append(node.left)
                    if node.right is not None:
                        q.append(node.right)
                    levelSize -= 1
                l2.append(l1)
            return l2[::-1]
