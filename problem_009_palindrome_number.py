class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or \
           (x % 10 == 0 and x > 0):
            return False

        half = 0
        while x > half:
            half = half * 10 + x % 10
            x //= 10

        return x == half or x == half // 10

    def isPalindrome_simple_python(self, x: int) -> bool:
        if x < 0:
            return False
        return x == int(str(x)[::-1])


if __name__ == "__main__":
    sol_class = Solution()
    ans = sol_class.isPalindrome(1251)
    print(ans)