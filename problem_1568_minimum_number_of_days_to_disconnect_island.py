from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, visited):
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                visited.add((r, c))
                for rn, cn in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if rn < 0 or cn < 0 or rn > rows-1 or cn > cols-1 or \
                       (rn, cn) in visited or grid[rn][cn] == 0:
                        continue
                    stack.append((rn, cn))

        visited = set()
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r, c) not in visited:
                    dfs(r, c, visited)
                    count += 1

        if count == 0 or count >= 2:
            return 0

        land = list(visited)
        for rl, cl in land:
            grid[rl][cl] = 0

            visited = set()
            count = 0
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] and (r, c) not in visited:
                        dfs(r, c, visited)
                        count += 1
            if count != 1:
                return 1
            grid[rl][cl] = 1

        return 2


if __name__ == "__main__":
    s = Solution()
    grid = [[1,1,0,0,1,1,0,1,0,1,1,1,1],
            [1,1,0,1,0,1,1,0,1,1,1,0,0],
            [0,0,1,1,1,0,0,1,1,1,1,0,0],
            [1,1,1,0,1,0,1,1,1,1,1,1,1],
            [1,1,1,0,1,1,0,1,1,1,1,0,1],
            [0,0,1,1,1,1,1,1,1,1,0,1,1],
            [1,1,1,0,0,1,1,1,0,1,1,1,1],
            [0,1,1,1,1,1,1,1,1,0,1,0,0],
            [1,1,1,1,1,1,1,1,0,0,1,0,1],
            [1,0,1,1,1,1,0,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1,1,0,1],
            [1,1,0,1,1,0,1,0,1,1,1,1,0],
            [1,0,1,1,1,1,1,1,1,1,1,0,1],
            [1,1,0,1,1,1,1,0,1,1,0,1,1],
            [1,0,1,1,1,1,1,1,1,1,1,0,1]]
    grid = [[1,0,1,0]]
    res = s.minDays(grid)
    print(res)