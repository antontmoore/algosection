from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        answers = [0] * n
        for i in range(n):
            cur = temperatures[i]
            while stack and cur > temperatures[stack[-1]]:
                k = stack.pop()
                answers[k] = i - k
            stack.append(i)
        return answers