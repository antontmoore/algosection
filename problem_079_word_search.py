from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(cell: tuple[int], idx: int):
            i, j = cell
            if board[i][j] != word[idx]:
                return False
            elif idx == len(word) - 1:
                return True
            else:
                move_up, move_down, move_left, move_right = False, False, False, False
                used.add(cell)
                if i > 0 and (i - 1, j) not in used:
                    move_up = dfs((i - 1, j), idx + 1)

                if i < m - 1 and (i + 1, j) not in used:
                    move_down = dfs((i + 1, j), idx + 1)

                if j > 0 and (i, j - 1) not in used:
                    move_left = dfs((i, j - 1), idx + 1)

                if j < n - 1 and (i, j + 1) not in used:
                    move_right = dfs((i, j + 1), idx + 1)

                if cell in used:
                    used.remove(cell)

                return move_up or move_down or move_left or move_right

        for start_i in range(m):
            for start_j in range(n):
                used = set()
                flag = dfs((start_i, start_j), 0)
                if flag:
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCB"
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"

    print(s.exist(board, word))