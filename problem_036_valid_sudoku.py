from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check strings
        for s in board:
            nums = [int(c) for c in s if c != '.']
            if len(nums) != len(set(nums)):
                return False

        # transpose
        board = list(map(list, zip(*board)))
        # check columns
        for s in board:
            nums = [int(c) for c in s if c != '.']
            if len(nums) != len(set(nums)):
                return False

        # check squares
        for box_str in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
            for box_col in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
                nums = [int(board[i][j]) for i in box_str for j in box_col if board[i][j] != '.']
                if len(nums) != len(set(nums)):
                    return False

        return True


if __name__ == "__main__":
    s = Solution()
    board =[
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    ans = s.isValidSudoku(board)
    print(ans)
