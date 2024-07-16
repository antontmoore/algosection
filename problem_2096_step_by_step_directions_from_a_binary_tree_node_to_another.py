from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def findPath(root, key_to_find, path, came_from):
            if not root:
                return False
            path.append((root.val, came_from))

            if root.val == key_to_find:
                return True

            if root.left and findPath(root.left, key_to_find, path, 'L'):
                return True

            if root.right and findPath(root.right, key_to_find, path, 'R'):
                return True

            path.pop()
            return False

        path_to_start = []
        path_to_end = []
        findPath(root, startValue, path_to_start, '')
        findPath(root, destValue, path_to_end, '')

        j = 0
        while j < len(path_to_start) and j < len(path_to_end):
            if path_to_start[j] != path_to_end[j]:
                break
            j += 1

        return "".join(['U' for i in range(j, len(path_to_start))]) + \
               "".join([path_to_end[i][1] for i in range(j, len(path_to_end))])


if __name__ == "__main__":
    s = Solution()

    node3, node6, node4 = TreeNode(3), TreeNode(6), TreeNode(4)
    node1, node2 = TreeNode(1, left=node3), TreeNode(2, left=node6, right=node4)
    node5 = TreeNode(5, left=node1, right=node2)
    res = s.getDirections(node5, 3, 6)

    # node1 = TreeNode(1)
    # node2 = TreeNode(2, left=node1)
    # res = s.getDirections(node2, 2, 1)
    print(res)
