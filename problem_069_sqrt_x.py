class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        left = 0
        right = x
        while right - left > 1:
            mid = (left + right) // 2


            if mid * mid > x:
                right = mid
            else:
                left = mid

        return left


if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(15))