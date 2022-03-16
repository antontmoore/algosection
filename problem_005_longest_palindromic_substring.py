class Solution:
    def longestPalindrome(self, s: str) -> str:

        # abba
        # dcd

        n = len(s)
        max_len = 1
        start = 0

        dp = [[False for j in range(n)] for i in range(n)]

        for i in range(n):
            dp[i][i] = True
            if i < n - 1 and s[i] == s[i+1]:
                dp[i][i+1] = True
                max_len = 2
                start = i

        k = 3  # palindrome length
        while k <= n:
            i = 0
            while i + k - 1 < n:
                j = i + k - 1

                if dp[i+1][j-1] is True and s[i] == s[j]:
                    dp[i][j] = True

                    if k > max_len:
                        max_len = k
                        start = i
                i += 1
            k += 1

        return s[start: start + max_len]


if __name__ == "__main__":
    sol_class = Solution()
    ans = sol_class.longestPalindrome("c")
    print(ans)