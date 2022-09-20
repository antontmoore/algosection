from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(subset=[], start=0):
            res.append(subset[:])

            for j in range(start, len(nums)):
                subset.append(nums[j])
                backtracking(subset, j + 1)
                subset.pop()

        backtracking()
        return res


if __name__ == "__main__":
    s = Solution()
    res = s.subsets([1, 2, 3])
    print(res)