from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1::] = nums[:i:-1]

        else:
            nums[::] = nums[::-1]


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3]
    # nums = [3, 2, 1]
    # nums = [1, 1, 5]
    nums = [1, 2, 3, 1, 4, 3, 2]
    s.nextPermutation(nums)
    print(nums)
