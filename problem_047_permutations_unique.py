from typing import List


class Solution:

    def recursivepick(self, cur_perm, morenums, perms):
        if len(morenums) == 0:
            perms.add(tuple(cur_perm))
            return

        for idx in range(len(morenums)):
            val = morenums[idx]
            lostnums = morenums.copy()
            lostnums.remove(val)
            self.recursivepick(cur_perm + [val], lostnums, perms)


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = set()
        self.recursivepick([], nums, perms)
        return list(map(list, perms))


if __name__ == "__main__":
    s = Solution()
    res = s.permuteUnique([1, 1, 2])
    print(res)
