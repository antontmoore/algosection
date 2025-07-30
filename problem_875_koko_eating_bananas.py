from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(max(piles), len(piles))

        def eatable(k, h):
            need_time = sum([p // k + 1 if p % k else p // k for p in piles])
            return need_time <= h

        while l < r:
            m = (l + r) // 2
            if eatable(m, h):
                r = m
            else:
                l = m + 1

        return r