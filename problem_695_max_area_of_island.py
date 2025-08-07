from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        seen = set()

        def dfs(r, c):
            if (r < 0 or r > m - 1 or c < 0 or c > n - 1 or grid[r][c] == 0 or (r, c) in seen):
                return 0

            seen.add((r, c))

            return (
                    1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
            )

        max_area = 0
        for i in range(m):
            for j in range(n):
                this = dfs(i, j)
                max_area = max(max_area, this)

        return max_area


if __name__ == "__main__":
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    s = Solution()
    res = s.maxAreaOfIsland(grid)
    print(res)
