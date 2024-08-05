from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for j, c in enumerate(citations):
            if c < j + 1:
                return j

        return len(citations)


if __name__ == "__main__":
    s = Solution()
    res = s.hIndex([3, 0, 6, 1, 5])
    res = s.hIndex([300, 300, 300])

    print(res)
