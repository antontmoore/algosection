from typing import List
from heapq import heappush, heappop, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapify(stones)
        while len(stones) > 1:
            stone1 = heappop(stones)
            stone2 = heappop(stones)
            if stone1 == stone2:
                continue
            else:
                heappush(stones, stone1 - stone2)
        return -stones[0] if stones else 0