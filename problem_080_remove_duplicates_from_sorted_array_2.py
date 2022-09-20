class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        old, new = 0, 0
        counter = 1

        for old in range(1, len(nums)):
            if nums[old] == nums[new]:
                counter += 1
            else:
                counter = 1

            if counter <= 2:
                new += 1
                nums[new] = nums[old]

        for j in range(new + 1, len(nums)):
            nums[j] = "_"

        return new + 1