from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:

        parents_by_val = {}
        children_by_val = {}
        for d in descriptions:
            p, c, l = d
            parents_by_val[c] = p
            if p not in children_by_val:
                children_by_val[p] = [-1, -1]
            children_by_val[p][1-l] = c

        head_val = 0
        for p in parents_by_val.values():
            if p not in parents_by_val:
                head_val = p

        head = TreeNode(val=head_val)
        node = head
        stack = [node]
        while stack:
            node = stack.pop()
            child_left, child_right = children_by_val[node.val] if node.val in children_by_val else [-1, -1]
            if child_left > 0:
                node.left = TreeNode(val=child_left)
                stack.append(node.left)
            if child_right > 0:
                node.right = TreeNode(val=child_right)
                stack.append(node.right)

        return head


if __name__ == "__main__":
    s = Solution()
    res = s.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])