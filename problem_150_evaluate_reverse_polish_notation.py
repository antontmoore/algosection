from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()
                if t == "+":
                    val = a + b
                elif t == "-":
                    val = a - b
                elif t == "*":
                    val = a * b
                else:
                    val = a / b
                stack.append(int(val))
            else:
                stack.append(int(t))
        return stack.pop()


if __name__ == "__main__":
    s = Solution()
    res = s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    print(res)
