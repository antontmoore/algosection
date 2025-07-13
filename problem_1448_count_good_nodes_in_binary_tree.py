from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def helper(node: TreeNode, max_val: int) -> None:
            if node is None:
                return

            if node.val >= max_val:
                nonlocal good
                good += 1

            helper(node.left, max(max_val, node.val))
            helper(node.right, max(max_val, node.val))

        helper(root, -100500)
        return good
