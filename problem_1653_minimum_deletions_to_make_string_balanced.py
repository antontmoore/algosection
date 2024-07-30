class Solution:
    def minimumDeletions(self, s: str) -> int:
        # prefix = [0] * len(s)
        suffix = [0] * len(s)
        #
        # for j, c in enumerate(s):
        #     prefix[j] = prefix[j - 1] + 1 if c == 'b' else prefix[j - 1]

        for j in range(len(s) - 2, -1, -1):
            suffix[j] = suffix[j + 1]
            suffix[j] += 1 if s[j + 1] == 'a' else 0

        min_removes = len(s) + 1
        count_b_left = 0
        for boundary in range(len(s)):
            removes = count_b_left + suffix[boundary]
            min_removes = min(min_removes, removes)
            if s[boundary] == 'b':
                count_b_left += 1

        return min_removes


if __name__ == "__main__":
    s = Solution()
    # res = s.minimumDeletions("aababbab")
    res = s.minimumDeletions("babaa")
    print(res)
