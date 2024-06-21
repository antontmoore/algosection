from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        cur_lost_sum = sum([customers[i] if grumpy[i] else 0 for i in range(minutes)])
        max_lost_sum = cur_lost_sum
        max_index = 0

        for j in range(minutes, len(customers)):
            cur_lost_sum += customers[j] if grumpy[j] else 0
            cur_lost_sum -= customers[j - minutes] if grumpy[j - minutes] else 0

            if cur_lost_sum > max_lost_sum:
                max_lost_sum = cur_lost_sum
                max_index = j - minutes + 1

        ans = 0
        for j in range(len(customers)):
            if grumpy[j] == 0 or (max_index <= j < max_index + minutes):
                ans += customers[j]

        return max_index

if __name__ == "__main__":
    s = Solution()
    ans = s.maxSatisfied([1, 0, 1, 2, 1, 1, 7, 5],
                         [0, 1, 0, 1, 0, 1, 0, 1], 3)
    print(ans)