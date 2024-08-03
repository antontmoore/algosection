from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = {}
        for elem in target:
            count[elem] = count.get(elem, 0) + 1

        for elem in arr:
            if elem not in count or count[elem] == 0:
                return False
            count[elem] -= 1

        return True