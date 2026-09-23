# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def rec_d(node, d):
            if node == None:
                return d-1
            else:
                d_left = rec_d(node.left, d+1)
                d_right = rec_d(node.right, d+1)
                return max(d_left, d_right)
        
        return rec_d(root, 1)