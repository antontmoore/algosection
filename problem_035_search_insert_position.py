from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        if target > nums[left]:
            left += 1
        return left


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 7
    s = Solution()
    ans = s.searchInsert(nums, target)
    print(ans)