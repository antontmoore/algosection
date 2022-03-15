class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2 ** 31 - 1
        min_int = -2 ** 31

        flag_minus = x < 0
        x = abs(x)

        rev = 0
        while x > 0:
            pop = x % 10
            x //= 10

            rev = 10 * rev + pop
            if (rev > max_int and not flag_minus) or \
                    (rev > -min_int and flag_minus):
                return 0

        if flag_minus:
            rev *= -1
        return rev

    def reverse_simple_for_python(self, x: int) -> int:
        if x >= 0:
            res = int(str(x)[::-1])
        else:
            res = -1 * int(str(x)[1:][::-1])

        if -2 ** 31 <= res <= 2 ** 31 - 1:
            return res
        else:
            return 0


if __name__ == "__main__":
    sol_class = Solution()
    ans = sol_class.reverse(123)
    print(ans)