
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        product = 0

        for j in range(len(num2)-1, -1, -1):
            order2 = len(num2) - 1 - j
            shift = 0
            for i in range(len(num1)-1, -1, -1):
                order1 = len(num1) - 1 - i
                p = int(num1[i]) * int(num2[j]) + shift
                if p < 10:
                    shift = 0
                else:
                    shift = p // 10
                    p = p % 10

                product += p * (10 ** (order1 + order2))
            product += shift * (10 ** (order1 + order2 + 1))

        first = ''

        return first + str(product)


if __name__ == "__main__":
    s = Solution()
    res = s.multiply("999", "999")
    print(res)