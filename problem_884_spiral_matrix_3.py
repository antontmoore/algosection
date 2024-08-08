from typing import List

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        res = []
        r, c = rStart, cStart
        steps = 1
        i = 0  # current directions
        while len(res) < rows * cols:
            for x in range(2):
                # twice with the same number of steps
                dr, dc = directions[i]
                for _ in range(steps):
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                    r, c = r + dr, c + dc

                i = (i + 1) % 4
            steps += 1

        return res


if __name__ == "__main__":
    s = Solution()
    res = s.spiralMatrixIII(5, 6, 1, 4)
    print(res)