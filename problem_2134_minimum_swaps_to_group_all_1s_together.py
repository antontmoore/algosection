from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        total_zeros = len(nums) - total_ones
        cur_ones = sum(nums[:total_ones])
        min_swaps = 2 * len(nums)
        for start in range(len(nums)):
            swaps = total_ones - cur_ones
            min_swaps = min(swaps, min_swaps)

            end = start + total_ones - 1
            if end < len(nums) - 1:
                cur_ones += nums[end + 1] - nums[start]
            else:
                delta = total_ones - (len(nums) - start - 1)
                cur_ones += nums[delta - 1] - nums[start]

        return min_swaps


if __name__ == "__main__":
    nums =[1, 1, 0, 0, 1]
    s = Solution()
    res = s.minSwaps(nums)
    print(res)