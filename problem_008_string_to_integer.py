class Solution:
    def myAtoi(self, s: str) -> int:
        min_int, max_int = -2 ** 31, 2 ** 31 - 1
        n = len(s)
        value = 0
        value_sign = +1
        index = 0

        while index < n and s[index] is " ":
            index += 1

        if index < n and s[index] == "-":
            value_sign = -1
            index += 1
        elif index < n and s[index] == "+":
            value_sign = 1
            index += 1

        while index < n and s[index].isdigit():
            value = value * 10 + int(s[index])
            index += 1

        value = value * value_sign
        if value < min_int:
            return min_int
        elif value > max_int:
            return max_int
        else:
            return value


if __name__ == "__main__":
    sol_class = Solution()
    ans = sol_class.myAtoi("2")
    print(ans)