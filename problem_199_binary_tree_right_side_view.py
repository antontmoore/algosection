from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        rightside = []
        next_level = deque([root])

        while next_level:

            # have where to go
            cur_level = next_level
            next_level = deque()

            while cur_level:
                cur_node = cur_level.popleft()
                if cur_node.left:
                    next_level.append(cur_node.left)
                if cur_node.right:
                    next_level.append(cur_node.right)

            rightside.append(cur_node.val)
        return rightside