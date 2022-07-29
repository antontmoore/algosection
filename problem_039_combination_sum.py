from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []
        def backtrack(cands, start_from, target, current_list):
            if target < 0:
                return

            if target == 0:
                out.append(current_list)
                return

            for j in range(start_from, len(cands)):
                backtrack(cands, j, target-cands[j], current_list + [cands[j]])

        backtrack(candidates, 0, target, [])
        return out


if __name__ == "__main__":
    nums = [2, 3, 6, 7]
    target = 7
    sol = Solution()
    ans = sol.combinationSum(nums, target)
    print(ans)

                        



