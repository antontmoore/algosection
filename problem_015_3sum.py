from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        have_met = dict()
        triples = set()
        for i, a in enumerate(nums[:-1]):
            if a in have_met:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] > -a:
                    right -= 1
                elif nums[left] + nums[right] < -a:
                    left += 1
                else:
                    triples.add((a, nums[left], nums[right]))
                    have_met[a] = True
                    left += 1

        return [list(triple) for triple in triples]


if __name__ == "__main__":
    sol_class = Solution()
    ans = sol_class.threeSum([-1, 0, 1, 2, -1, -4])
    print(ans)
