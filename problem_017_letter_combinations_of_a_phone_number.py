from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_letters = {"1": "", "2": "abc", "3": "def",
                             "4": "ghi", "5": "jkl", "6": "mno",
                             "7": "pqrs", "8": "tuv", "9": "wxyz"}

        if len(digits) == 0:
            return []

        res = []

        def give_combs(l, s):

            if l == len(digits):
                res.append(s)
                return

            for letter in digits_to_letters[digits[l]]:
                give_combs(l + 1, s + letter)

        give_combs(0, '')
        return res
