from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])
        number_of_islands = 0

        def dfs(grid, sp):
            node_q = [sp]
            while node_q:
                ni, nj = node_q.pop()
                if ni > 0 and grid[ni - 1][nj] == '1':
                    node_q.append((ni - 1, nj))
                if ni < m - 1 and grid[ni + 1][nj] == '1':
                    node_q.append((ni + 1, nj))
                if nj > 0 and grid[ni][nj - 1] == '1':
                    node_q.append((ni, nj - 1))
                if nj < n - 1 and grid[ni][nj + 1] == '1':
                    node_q.append((ni, nj + 1))
                grid[ni][nj] = '0'

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    number_of_islands += 1
                    dfs(grid, (i, j))

        return number_of_islands


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    s = Solution()
    noi = s.numIslands(grid)
    print(noi)