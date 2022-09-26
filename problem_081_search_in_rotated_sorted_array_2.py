from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[left] == nums[mid] and nums[right] == nums[mid]:
                left += 1
                right -= 1

            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1


        return False


if __name__ == "__main__":
    s = Solution()
    nums = [1, 0, 1, 1, 1]
    target = 0
    res = s.search(nums, target)
    print(res)

