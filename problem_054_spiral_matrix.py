from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while len(matrix) > 0:
            topstring = matrix.pop(0)
            res += topstring
            matrix = [st[::-1] for st in matrix]
            matrix = list(zip(*matrix))
        return res


if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(s.spiralOrder(matrix))