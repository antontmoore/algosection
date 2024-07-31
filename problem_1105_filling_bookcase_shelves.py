from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [0] * (len(books) + 1)

        for i in range(len(books) - 1, -1, -1):
            cur_width = shelfWidth
            max_height = 0
            dp[i] = float("inf")
            for j in range(i, len(books)):
                width, height = books[j]
                if cur_width < width:
                    break
                cur_width -= width
                max_height = max(max_height, height)
                dp[i] = min(
                    dp[i],
                    dp[j + 1] + max_height
                )
        return dp[0]


if __name__ == "__main__":
    s = Solution()
    books, shelf_width = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4
    res = s.minHeightShelves(books, shelf_width)
    print(res)