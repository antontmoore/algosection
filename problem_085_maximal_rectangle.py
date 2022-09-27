from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def find_max_area(hs):

            max_area = 0
            stack = []
            for i, h in enumerate(hs):
                start = i
                while len(stack) > 0 and stack[-1][1] > h:
                    poped_index, poped_height = stack.pop()
                    max_area = max(max_area, poped_height * (i - poped_index))
                    start = poped_index
                stack.append((start, h))

            for i, h in stack:
                max_area = max(max_area, h * (len(hs) - i))

            return max_area


        m, n = len(matrix), len(matrix[0])
        max_rectangle = 0
        heights = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1

            max_rectangle = max(max_rectangle, find_max_area(heights))

        return max_rectangle


if __name__ == "__main__":
    s = Solution()
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]
              ]
    matrix = [["1"]]
    matrix = [["0", "1"],
              ["1", "0"]
              ]

    print(s.maximalRectangle(matrix))
