from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n = len(matrix[0])
        # looking for the row
        top, bottom = 0, len(matrix)-1

        while top <= bottom:
            row = (top + bottom) // 2

            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        # looking for the column
        left, right = 0, len(matrix[0])-1

        while right > left:
            mid = (left + right) // 2

            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return matrix[row][left] == target


if __name__ == "__main__":
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target = 13
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 8
    s = Solution()
    print(s.searchMatrix(matrix, target))