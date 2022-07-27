from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(arr, left, right, target):
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left if target == arr[left] else -1

        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # sorted in right part
                if nums[mid] <= target <= nums[right]:
                    return binary_search(nums, mid, right, target)
                else:
                    # but we need to go to the left
                    right = mid

            elif nums[left] <= nums[mid]:
                # sorted in left part
                if nums[left] <= target <= nums[mid]:
                    return binary_search(nums, left, mid, target)
                else:
                    # but we need to go to the right
                    left = mid+1

        return left if target == nums[left] else -1


if __name__ == "__main__":
    s = Solution()
    nums = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
    ans = s.search(nums, 10)
    print(ans)
