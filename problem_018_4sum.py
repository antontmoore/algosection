from typing import  List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)
        n = len(nums)
        fours = set()

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                a = nums[i]
                b = nums[j]

                l = j + 1
                r = n - 1

                while r > l:
                    if a + b + nums[l] + nums[r] == target:
                        four_ind = [i, j, l, r]
                        fours.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1

                    if a + b + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1

        return sorted([list(f) for f in fours])


if __name__ == "__main__":
    sol_class = Solution()
    ans = sol_class.fourSum([1, 0, -1, 0, -2, 2], 0)
    print(ans)