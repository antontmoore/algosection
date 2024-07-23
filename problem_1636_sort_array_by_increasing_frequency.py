from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = {}
        for elem in nums:
            count[elem] = count.get(elem, 0) + 1

        nums.sort(key=lambda x: (count[x],-x))
        return nums


if __name__ == "__main__":
    nums = [1, 1, 2, 2, 2, 3]
    s = Solution()
    res = s.frequencySort(nums)
    print(res)
