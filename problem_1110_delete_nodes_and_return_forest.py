from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res_set = set([root])

        def dfs(node):
            if not node:
                return None
            res = node
            if node.val in to_delete:
                res = None
                res_set.discard(node)

                if node.left: res_set.add(node.left)
                if node.right: res_set.add(node.right)
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            return res

        dfs(root)
        return list(res_set)


if __name__ == "__main__":
    s = Solution()
    node4, node5, node6, node7 = TreeNode(4), TreeNode(5), TreeNode(6), TreeNode(7)
    node2, node3 = TreeNode(2, left=node4, right=node5), TreeNode(3, left=node6, right=node7)
    node1 = TreeNode(1, left=node2, right=node3)


    ans = s.delNodes(node1, [3, 5])
    print([a.val for a in ans])