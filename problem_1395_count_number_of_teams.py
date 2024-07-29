from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        total_teams = 0
        for j in range(1, len(rating) - 1):
            smaller_left, larger_right = 0, 0
            for i in range(j):
                if rating[i] < rating[j]:
                    smaller_left += 1
            for k in range(j + 1, len(rating)):
                if rating[j] < rating[k]:
                    larger_right += 1

            total_teams += smaller_left * larger_right
            total_teams += (j - smaller_left) * (len(rating) - j - 1 - larger_right)
        return total_teams
