class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_len = 0
        for j in set_nums:
            if j - 1 not in set_nums:
                k = 1
                while j + k in set_nums:
                    k += 1

                max_len = max(max_len, k)
        return max_len