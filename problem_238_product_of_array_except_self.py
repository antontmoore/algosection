from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1 for _ in range(n)]
        suffix = [1 for _ in range(n)]
        result = [1 for _ in range(n)]
        for j in range(n):
            prefix[j] = nums[j] if j == 0 else prefix[j-1] * nums[j]
            suffix[n - j - 1] = nums[n - 1] if j == 0 else suffix[n - j] * nums[n - j - 1]

        for j in range(n):
            if j > 0:
                result[j] *= prefix[j - 1]
            if j < n - 1:
                result[j] *= suffix[j + 1]
        return result