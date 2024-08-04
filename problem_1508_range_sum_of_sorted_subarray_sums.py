from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        all_sums = []
        for start in range(n):
            cumsum = nums[start]
            all_sums.append(nums[start])
            for j in range(start + 1, n):
                cumsum += nums[j] % (10 ** 9 + 7)
                all_sums.append(cumsum)
        all_sums.sort()
        return sum(all_sums[left - 1: right]) % (10 ** 9 + 7)
