from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return node

        visited = dict()

        def dfs(node):
            if node in visited:
                return visited[node]

            nodecopy = Node(val=node.val, neighbors=[])
            visited[node] = nodecopy

            for neighb in node.neighbors:
                neighbcopy = dfs(neighb)
                nodecopy.neighbors.append(neighbcopy)

            return nodecopy

        return dfs(node)
