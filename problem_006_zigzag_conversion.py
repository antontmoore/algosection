class Solution:
    def convert(self, s: str, numRows: int) -> str:

        l = ['' for _ in range(numRows)]
        for idx, c in enumerate(s):
            row = idx % (2 * numRows - 2)
            if row > numRows - 1:
                delta = row - numRows + 1
                row = (numRows - 1) - delta
            l[row] += c

        return ''.join(l)


if __name__ == "__main__":
    sol_class = Solution()
    ans = sol_class.convert("PAYPALISHIRING", 3)
    print(ans)