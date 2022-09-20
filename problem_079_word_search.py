from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(row, col, w, used):
            if len(w) == 0:
                return True

            flag = False
            if row > 0 and board[row-1][col] == w[0] and (row-1, col) not in used:
                used.add((row - 1, col))
                flag |= backtrack(row-1, col, w[1:], used)
                used.remove((row-1, col))

            if col > 0 and board[row][col-1] == w[0] and (row, col-1) not in used:
                used.add((row, col - 1))
                flag |= backtrack(row, col-1, w[1:], used)
                used.remove((row, col - 1))

            if row < m-1 and board[row+1][col] == w[0] and (row+1, col) not in used:
                used.add((row + 1, col))
                flag |= backtrack(row+1, col, w[1:], used)
                used.remove((row + 1, col))

            if col < n-1 and board[row][col+1] == w[0] and (row, col+1) not in used:
                used.add((row, col + 1))
                flag |= backtrack(row, col+1, w[1:], used)
                used.remove((row, col + 1))

            return flag


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    used = set()
                    used.add((i, j))
                    flag = backtrack(i, j, word[1:], used)
                    if flag: return flag

        return False


if __name__ == "__main__":
    s = Solution()
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCB"
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"

    print(s.exist(board, word))