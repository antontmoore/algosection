from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        N = len(rowSum)
        M = len(colSum)

        matrix = [[0] * M for _ in range(N)]
        i, j = 0, 0

        while i < N and j < M:
            matrix[i][j] = min(rowSum[i], colSum[j])

            rowSum[i] -= matrix[i][j]
            colSum[j] -= matrix[i][j]

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1

        return matrix


if __name__ == "__main__":
    s = Solution()
    res = s.restoreMatrix([3, 8], [4, 7])
    res = s.restoreMatrix([5, 7, 10], [8, 6, 8])
    print(*res)
