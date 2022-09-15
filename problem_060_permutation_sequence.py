class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1, 1]
        for j in range(2, 10):
            factorials.append(factorials[-1] * j)

        res = ''
        digits = [j+1 for j in range(n)]
        for j in range(1, n+1):
            index = int(k / factorials[n-1])
            if k % factorials[n-1] == 0:
                index -= 1
            res += str(digits[index])
            digits.pop(index)
            k -= factorials[n-1] * index
            n -= 1

        return res


if __name__ == "__main__":
    s = Solution()
    m = s.getPermutation(4, 9)
    print(m)
