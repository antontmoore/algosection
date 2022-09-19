from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums)-1
        idx = l
        while idx <= r:

            if nums[idx] == 0:
                nums[l], nums[idx] = nums[idx], nums[l]
                l += 1
            if nums[idx] == 2:
                nums[r], nums[idx] = nums[idx], nums[r]
                r -= 1
                idx -= 1

            idx += 1





if __name__ == "__main__":
    nums = [2, 0, 1, 1, 2, 0, 1, 1, 0]
    s = Solution()
    s.sortColors(nums)
    print(nums)