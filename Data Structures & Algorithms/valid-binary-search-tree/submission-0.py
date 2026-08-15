# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def check(node, minBound, maxBound):
            if node is None:
                return True
            if minBound is not None and node.val < minBound:
                return False
            if maxBound is not None and node.val > maxBound:
                return False
            return check(node.left, minBound, node.val - 1) and check(node.right, node.val + 1, maxBound)
        
        
        return check(root, None, None)