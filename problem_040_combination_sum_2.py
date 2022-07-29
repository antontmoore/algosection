from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        out = []
        candidates = sorted(candidates)

        def backtracking(cands, target, current_list, current_index):

            if target < 0:
                return

            if target == 0:
                out.append(current_list)

            for j in range(current_index, len(cands)):
                if j > current_index and cands[j] == cands[j-1]:
                    continue

                if cands[j] > target:
                    break
                backtracking(cands, target-cands[j], current_list + [cands[j]], j+1)

        backtracking(candidates, target, [], 0)
        out = list(map(list, out))
        return out


if __name__ == "__main__":
    nums = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    sol = Solution()
    ans = sol.combinationSum2(nums, target)
    print(ans)




