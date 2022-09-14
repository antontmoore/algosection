from typing import List


class Solution:
    variants: float = 0
    def totalNQueens(self, n: int) -> List[List[str]]:

        def backtrack(field_dict, row):
            if row == n:
                self.variants += 1
                return

            for col in range(n):
                if col in field_dict:
                    continue

                found_diag = False
                for col_occ, row_occ in field_dict.items():
                    if abs(row - row_occ) == abs(col - col_occ):
                        found_diag = True
                        break
                if found_diag:
                    continue

                # good position to place queen
                new_field_dict = field_dict.copy()
                new_field_dict[col] = row
                backtrack(new_field_dict, row+1)

        empty_field = dict()  # key = col, val = row
        backtrack(empty_field, 0)

        return self.variants


if __name__ == "__main__":
    s = Solution()
    print(s.totalNQueens(4))
