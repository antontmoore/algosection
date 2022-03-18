class Solution:
    def intToRoman(self, num: int) -> str:

        def digit_to_chars(digit, s, f, b):
            if digit <= 3:
                return s * digit
            elif digit == 4:
                return s + f
            elif digit <= 8:
                return f + s * (digit - 5)
            elif digit == 9:
                return s + b
            else:
                print("digit is not correct")

        ans = ""
        thousands = num // 1000
        ans += "M" * thousands

        num %= 1000
        hundreds = num // 100
        ans += digit_to_chars(hundreds, "C", "D", "M")

        num %= 100
        tens = num // 10
        ans += digit_to_chars(tens, "X", "L", "C")

        ones = num % 10
        ans += digit_to_chars(ones, "I", "V", "X")

        return ans

