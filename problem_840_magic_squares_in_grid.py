from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0

        def is_magic(grid, rs, re, cs, ce):
            digits = set()
            for i in range(rs, re + 1):
                for j in range(cs, ce + 1):
                    if grid[i][j] > 9 or grid[i][j] <= 0:
                        return False
                    if grid[i][j] in digits:
                        return False
                    digits.add(grid[i][j])
            sc1 = sum([grid[j][cs] for j in range(rs, rs + 3)])
            sc2 = sum([grid[j][cs + 1] for j in range(rs, rs + 3)])
            sc3 = sum([grid[j][cs + 2] for j in range(rs, rs + 3)])
            sr1 = sum([grid[rs][j] for j in range(cs, cs + 3)])
            sr2 = sum([grid[rs + 1][j] for j in range(cs, cs + 3)])
            sr3 = sum([grid[rs + 2][j] for j in range(cs, cs + 3)])
            sd1 = sum([grid[rs + j][cs + j] for j in range(3)])
            sd2 = sum([grid[rs + j][ce - j] for j in range(3)])
            return sc1 == sc2 == sc3 == sr1 == sr2 == sr3 == sd1 == sd2

        total_squares = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if is_magic(grid, i, i + 2, j, j + 2):
                    total_squares += 1

        return total_squares