# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def check(node):
            if node is None:
                return 0, 0
            if node.left and node.right:
                d1, h1 = check(node.left)
                d2, h2 = check(node.right)
                return max(d1, d2, h1 + h2 + 2), max(h1, h2) + 1
            if node.left:
                d1, h1 = check(node.left)
                return max(d1, h1 + 1), h1 + 1
            if node.right:
                d1, h1 = check(node.right)
                return max(d1, h1 + 1), h1 + 1
            return 0, 0
                
        
        d, _ = check(root)
        return d