class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        counts = {}
        max_window = 0

        left = 0
        for right in range(n):
            counts[s[right]] = counts.get(s[right], 0) + 1

            while right - left + 1 - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)

        return max_window


if __name__ == "__main__":
    s = Solution()
    res = s.characterReplacement(s="AAAB", k=0)
    print(res)
