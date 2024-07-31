from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        buffer = nums[-k:]
        pos = 0
        for i in range(n):
            current_value = nums[i]
            nums[i] = buffer[pos]
            buffer[pos] = current_value
            pos = (pos + 1) % len(buffer)


if __name__ == "__main__":
    s = Solution()
    # s.rotate([1, 2, 3, 4, 5, 6, 7], 3)
    s.rotate([1, 2], 3)
