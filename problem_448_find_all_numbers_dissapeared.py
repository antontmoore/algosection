from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for number in nums:
            index = abs(number) - 1
            if nums[index] > 0:
                nums[index] *= -1

        missing_numbers = [i + 1 for i, x in enumerate(nums) if x > 0]

        return missing_numbers

if __name__ == '__main__':
    s = Solution()
    ans = s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
    print(ans)