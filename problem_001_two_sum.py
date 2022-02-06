from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_by_value = dict()  # int -> int
        for idx, value in enumerate(nums):
            pair_index = index_by_value.get(target - value, -1)
            if pair_index != -1:
                return [pair_index, idx]
            index_by_value[value] = idx
        return [0]
