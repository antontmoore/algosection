class Solution:
    def isValid(self, s: str) -> bool:

        pair = {"}": "{",
                "]": "[",
                ")": "("}
        c = ""
        for b in s:
            if b in "({[":
                c += b
            else:
                if len(c) == 0 or c[-1] != pair[b]:
                    return False
                else:
                    c = c[:-1]

        return len(c) == 0
