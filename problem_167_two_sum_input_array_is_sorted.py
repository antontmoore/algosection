from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            nsum = numbers[l] + numbers[r]
            if nsum == target:
                return [l + 1, r + 1]
            if nsum < target:
                l += 1
            else:
                r -= 1

        return [-1, -1]