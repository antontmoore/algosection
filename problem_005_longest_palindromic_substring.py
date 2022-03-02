class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [1] * len(s)
        for i in range(len(s)):
            if i > 0:
                if s[i] == s[i-1]:
                    dp[i] = 2

                j = i - dp[i - 1] - 1
                if j >= 0 and s[i] == s[j]:
                    dp[i] = dp[i - 1] + 2


        palindrom_length = max(dp)
        max_ind = dp.index(palindrom_length)
        return s[max_ind - palindrom_length + 1:max_ind + 1]


if __name__ == "__main__":
    s = Solution()
    input_string = "vvvvv"
    ans = s.longestPalindrome(input_string)
    print(ans)