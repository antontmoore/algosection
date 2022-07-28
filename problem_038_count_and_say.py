class Solution:

    def unroll(self, s: str):
        out = ''
        current = s[0]
        counter = 1
        for c in s[1:]:
            if current == c:
                counter += 1
            else:
                out += str(counter) + current
                current = c
                counter = 1
        out += str(counter) + current
        return out

    def countAndSay(self, n: int) -> str:
        out_str = ''
        for j in range(n):
            if j == 0:
                out_str = '1'
            else:
                out_str = self.unroll(out_str)
        return out_str


if __name__ == "__main__":
    sol = Solution()
    ans = sol.countAndSay(4)
    print(ans)
