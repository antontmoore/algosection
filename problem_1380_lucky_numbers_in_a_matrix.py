from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        min_row_value, max_col_value = [], []
        for i in range(m):
            min_row_value.append(min(matrix[i]))
        for j in range(n):
            max_col_value.append(max([matrix[i][j] for i in range(m)]))

        res = []
        for i in range(m):
            for j in range(n):
                if min_row_value[i] == max_col_value[j]:
                    res.append(min_row_value[i])
        return res
