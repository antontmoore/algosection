from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        start, end = 0, 1

        res = []

        for i in range(len(intervals)):
            if newInterval[end] < intervals[i][start]:
                return res + [newInterval] + intervals[i:]
            elif newInterval[start] > intervals[i][end]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[start], intervals[i][start]),
                               max(newInterval[end], intervals[i][end])]

        res.append(newInterval)

        return res


if __name__ == "__main__":
    s = Solution()
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]

    res = s.insert(intervals, newInterval)
    print(res)