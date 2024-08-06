class Solution:
    def minimumPushes(self, word: str) -> int:
        count = {}
        for c in word:
            count[c] = count.get(c, 0) + 1

        sorted_letters = sorted(count.items(), key=lambda x: - x[1])

        total_pushes = 0
        for sl_idx, sl in enumerate(sorted_letters):
            total_pushes += sl[1] * (sl_idx // 8 + 1)

        return total_pushes
