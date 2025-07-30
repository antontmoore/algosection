from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[left]:
                # left part is sorted
                if target < nums[mid] and target >= nums[left]:
                    # target inside left part
                    right = mid - 1
                else:
                    # let's look for it in the right part
                    left = mid + 1
            else:
                # right part is sorted
                if target > nums[mid] and target <= nums[right]:
                    # target inside right part
                    left = mid + 1
                else:
                    # let's look for it in left part
                    right = mid - 1
        return -1


if __name__ == "__main__":
    s = Solution()
    # nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
    nums = [3, 1]
    ans = s.search(nums, 1)
    print(ans)
