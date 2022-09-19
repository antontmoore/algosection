class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        zero_rows, zero_cols = set(), set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0
