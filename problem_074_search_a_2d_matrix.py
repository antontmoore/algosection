from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def idx(r, c):
            return r * n + c

        def rc(idx):
            return idx // n, idx % n

        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            row, col = rc(mid)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


if __name__ == "__main__":
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target = 13
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    matrix = [[1]]
    target = 8
    s = Solution()
    print(s.searchMatrix(matrix, target))