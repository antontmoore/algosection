from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp
        dp = [False] * len(nums)
        dp[0] = True
        for j in range(len(nums)):
            if not dp[j]:
                return False
            if nums[j] + j >= len(nums):
                return True
            for step in range(nums[j] + 1):
                if j + step < len(nums):
                    dp[j + step] = True

        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    res = s.canJump([2,3,1,1,4])
    print(res)

