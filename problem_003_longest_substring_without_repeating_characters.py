class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left, right = 0, 0
        ans = 0
        d = dict()

        for right in range(len(s)):
            if s[right] in d.keys():
                left = max(left, d[s[right]])

            ans = max(ans, right - left + 1)

            d[s[right]] = right + 1

        return ans
