from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = True
        def depth(node):
            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            if abs(left_depth - right_depth) > 1:
                nonlocal balanced
                balanced = False
            return max(left_depth, right_depth) + 1

        depth(root)
        return balanced
