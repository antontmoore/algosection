from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dp = [(p[0]**2 + p[1]**2, i) for i, p in enumerate(points)]
        heapq.heapify(dp)
        closest_k = heapq.nlargest(k, dp, key=lambda x: -x[0])
        return [points[i] for (_, i) in closest_k]
