from typing import List
from collections import defaultdict

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:

        index_map = defaultdict(list)
        n = len(arr)

        for i, value in enumerate(arr):
            index_map[value].append(i)

        answer = [0] * n
        for indices in index_map.values():
            m = len(indices)
            total_distance = sum(indices) - indices[0] * m
            for i, index in enumerate(indices):
                delta = indices[i] - indices[i - 1] if i >= 1 else 0
                total_distance += i * delta - (m - i) * delta

                answer[index] = total_distance

        return answer