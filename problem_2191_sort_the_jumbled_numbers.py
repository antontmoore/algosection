from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        pairs = []

        for idx, n in enumerate(nums):
            value = 0
            base = 1
            if n == 0:
                value = mapping[0]
            while n > 0:
                digit = n % 10
                n = n // 10
                value += mapping[digit] * base
                base *= 10

            pairs.append((value, idx))
        pairs.sort()

        return [nums[p[1]] for p in pairs]


if __name__ == "__main__":
    s = Solution()
    mapping, nums = [5,6,8,7,4,0,3,1,9,2], [7686,97012948,84234023,2212638,99]
    res = s.sortJumbled(mapping, nums)
    print(res)