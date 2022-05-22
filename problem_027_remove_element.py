from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        to_read = 0
        to_write = 0
        while to_read < len(nums):
            if nums[to_read] != val:
                nums[to_write] = nums[to_read]
                to_write += 1
            to_read += 1

        delta = to_write
        while to_write < len(nums):
            nums[to_write] = -1
            to_write += 1

        return delta