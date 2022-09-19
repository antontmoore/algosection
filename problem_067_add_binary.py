class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_len = max(len(a), len(b))
        a = '0' * (sum_len - len(a)) + a
        b = '0' * (sum_len - len(b)) + b

        shift = 0
        res = [0] * sum_len
        for j in range(sum_len - 1, -1, -1):
            digit = int(a[j]) + int(b[j]) + shift
            shift = digit // 2
            res[j] = str(digit % 2)

        res  = ''.join(res)
        if shift:
            res = '1' + res

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.addBinary('11', '1'))