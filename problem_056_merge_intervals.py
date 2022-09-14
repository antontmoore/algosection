from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        start, end = 0, 1
        intervals = sorted(intervals, key=lambda x: x[start])

        res = []
        current_interval = intervals[0]
        for interval in intervals[1:]:
            if current_interval[end] >= interval[start]:
                if interval[end] > current_interval[end]:
                    current_interval[end] = interval[end]
            else:
                res.append(current_interval)
                current_interval = interval
        res.append(current_interval)

        return res
