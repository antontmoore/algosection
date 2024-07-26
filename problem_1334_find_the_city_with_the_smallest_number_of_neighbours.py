from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        neighbours = defaultdict(set)
        for e in edges:
            neighbours[e[0]].add((e[1], e[2]))
            neighbours[e[1]].add((e[0], e[2]))

        def dijkstra(node, neighbours, distanceThreshold):
            nonlocal n
            reachable_nodes = set()
            distances = [1e6 + 1] * n
            distances[node] = 0
            # current_distance, node_number
            queue = []
            heappush(queue, (0, node))
            while queue:
                cur_dist, node = heappop(queue)
                if cur_dist > distances[node]:
                    continue

                for neighb, weight in neighbours[node]:
                    dist = cur_dist + weight
                    if dist < distances[neighb]:
                        if dist <= distanceThreshold:
                            distances[neighb] = dist
                            reachable_nodes.add(neighb)
                            heappush(queue, (dist, neighb))

            return reachable_nodes

        min_rn = n
        best_city = -1
        for node in range(n):
            rc = dijkstra(node, neighbours, distanceThreshold)
            if len(rc) <= min_rn:
                min_rn = len(rc)
                best_city = node

        return best_city

if __name__ == "__main__":
    # n = 4
    # edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    # distanceThreshold = 4

    n = 6
    edges = [[0,3,7],[2,4,1],[0,1,5],[2,3,10],[1,3,6],[1,2,1]]
    distanceThreshold = 417
    s = Solution()
    res = s.findTheCity(n, edges, distanceThreshold)
    print(res)
