class Solution:
    def grayCode(self, n: int) -> List[int]:

        res = [0]
        if n == 0: return res

        power = 0
        for power in range(n):
            to_add = [val + 2 ** power for val in res[::-1]]
            res.extend(to_add)

        return res