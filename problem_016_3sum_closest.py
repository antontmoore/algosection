from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)

        closest_value = 10 ** 8
        for i, a in enumerate(nums[:-1]):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum3 = a + nums[left] + nums[right]
                if abs(sum3 - target) < abs(closest_value - target):
                    closest_value = sum3

                if sum3 < target:
                    left += 1
                else:
                    right -= 1

        return closest_value
