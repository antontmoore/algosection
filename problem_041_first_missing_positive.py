from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            nums[i] = 0 if nums[i] < 0 else nums[i]

        for v in nums:
            val = abs(v)
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        for i, v in enumerate(nums):
            if v >= 0:
                return i + 1

        return len(nums) + 1


if __name__ == "__main__":
    s =  Solution()
    res = s.firstMissingPositive([1, 2, 0])
    print(res)