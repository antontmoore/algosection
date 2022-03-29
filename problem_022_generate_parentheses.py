from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def gen_par(opened: int, closed: int, s: str):
            if len(s) == 2 * n:
                ans.append(s)
                return

            if opened < n:
                gen_par(opened + 1, closed, s + "(")
            if closed < opened:
                gen_par(opened, closed + 1, s + ")")

        gen_par(0, 0, "")
        return ans
