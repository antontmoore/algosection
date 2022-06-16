class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        q = int(dividend / divisor)
        if q > 2**31 -1:
            return 2**31 -1
        if q < -(2**31):
            return -(2**31)
        else:
            return q
