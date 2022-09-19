class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        ways = [0, 1, 2] + [0] * (n - 2)
        for j in range(3, n + 1):
            ways[j] = ways[j - 1] + ways[j - 2]

        return ways[n]
