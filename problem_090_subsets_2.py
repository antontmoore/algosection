from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def backtrack(subset, idx=0):

            if idx == len(nums):
                res.append(subset[::])
                return

            subset.append(nums[idx])
            backtrack(subset, idx + 1)  # adding nums[idx]
            subset.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx+1]:
                idx += 1

            backtrack(subset, idx + 1)  # not adding nums[idx] and all the same

        backtrack([])
        return res



if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 2]
    print(s.subsetsWithDup(nums))

