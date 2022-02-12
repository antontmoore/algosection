class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left, right = 0, 0
        ans = 0
        have_already_met = dict()

        for right in range(len(s)):
            if s[right] in have_already_met.keys():
                left = max(left, have_already_met[s[right]] + 1)

            ans = max(ans, right - left + 1)

            have_already_met[s[right]] = right

        return ans

if __name__ == "__main__":
    s = Solution()
    s.lengthOfLongestSubstring("abba")