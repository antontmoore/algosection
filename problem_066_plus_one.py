from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        shift = 1
        for j in range(len(digits) - 1, -1, -1):
            new_digit = digits[j] + shift

            if new_digit == digits[j]:
                break

            shift = new_digit // 10
            digits[j] = new_digit % 10

        if shift:
            digits.insert(0, 1)
        return digits

