from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = list(range(n**2))
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        val = 1

        c1, c2 = 0, n-1
        r1, r2 = 0, n-1

        while (c1 <= c2 and r1 <= r2):
            for c in range(c1, c2+1):
                matrix[r1][c] = val
                val += 1

            for r in range(r1+1, r2+1):
                matrix[r][c2] = val
                val += 1

            if c1 < c2 and r1 < r2:
                for c in range(c2-1, c1-1, -1):
                    matrix[r2][c] = val
                    val += 1

                for r in range(r2-1, r1, -1):
                    matrix[r][c1] = val
                    val += 1

            r1, r2 = r1+1, r2-1
            c1, c2 = c1+1, c2-1

        return matrix



if __name__ == "__main__":
    s = Solution()
    m = s.generateMatrix(3)
    print(m)
