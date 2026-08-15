"""
dfs for p and q
common path
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        a = min(p.val, q.val)
        b = max(p.val, q.val)

        curr = root
        while curr:
            if a <= curr.val and b >= curr.val:
                return curr
            if a >= curr.val and b >= curr.val:
                curr = curr.right
            else:
                curr = curr.left

        return None

        