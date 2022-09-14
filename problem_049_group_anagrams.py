from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = dict()
        for s in strs:
            sorted_s = ''.join(sorted(s))
            d[sorted_s] = d.get(sorted_s, []) + [s]

        res = []
        for key, val in d.items():
            res.append(val)

        return res
