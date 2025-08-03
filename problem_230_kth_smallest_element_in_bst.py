from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        while True:
            # go left as much as we can
            while root:
                # put previous node on stack (as in recursive inorder traversal)
                stack.append(root)
                root = root.left
            # now we are at root = None (i.e. can't go left anymore)
            # go up by takin previous node form stack (it's like middle node in recursive)
            root = stack.pop()
            k -= 1
            if not k:
                return root.val

            # and go right (like in recursive)
            root = root.right
