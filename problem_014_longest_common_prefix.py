class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs[1:]:
            j = 0
            while j < len(prefix) and \
                    j < len(s) and \
                    s[j] == prefix[j]:
                j += 1

            prefix = prefix[:j]