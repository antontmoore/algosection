from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def array_to_tree(left, right):
            nonlocal preorder_idx
            if left > right:
                return None
            root = TreeNode(val=preorder[preorder_idx])
            preorder_idx += 1

            root.left = array_to_tree(left, inorder_idx_by_val[root.val] - 1)
            root.right = array_to_tree(inorder_idx_by_val[root.val] + 1, right)

            return root

        preorder_idx = 0
        inorder_idx_by_val = {}
        for idx, val in enumerate(inorder):
            inorder_idx_by_val[val] = idx

        return array_to_tree(0, len(inorder) - 1)
