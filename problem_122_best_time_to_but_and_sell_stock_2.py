from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for j in range(len(prices) - 1):
            if prices[j] < prices[j + 1]:
                profit += prices[j + 1] - prices[j]
        return profit
