from typing import List


class Solution:

    def recursivepick(self, cur_perm, morenums, perms):
        if len(morenums) == 0:
            perms.append(cur_perm)
            return

        for idx in range(len(morenums)):
            val = morenums[idx]
            lostnums = morenums.copy()
            lostnums.remove(val)
            self.recursivepick(cur_perm + [val], lostnums, perms)

    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        self.recursivepick([], nums, perms)
        return perms


if __name__ == "__main__":
    s = Solution()
    res = s.permute([1, 2, 3])
    print(res)



