from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while left < right and not (nums[left] == target and nums[right] == target):
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                if nums[left] < target:
                    left += 1
                if nums[right] > target:
                    right -= 1

        return [left, right] if len(nums) > 0 and nums[left] == target else [-1, -1]


if __name__ == "__main__":
    s = Solution()
    ans = s.searchRange([], 5)
    print(ans)




