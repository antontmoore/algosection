from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [100 * len(nums)] * len(nums)
        dp[0] = 0
        for i, num in enumerate(nums):
            for j in range(1, num + 1):
                if i + j > len(dp) - 1:
                    break
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]

if __name__ == "__main__":
    s = Solution()
    res = s.jump([2, 3, 1, 1, 4])
    print(res)