from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [y[0] for y in sorted(list(zip(names, heights)), key=lambda x: -x[1])]