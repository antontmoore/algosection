from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        left_index, right_index = 0, len(height)-1
        max_left = height[0]
        max_right = height[len(height) - 1]
        res = 0

        while left_index < right_index:
            if max_left <= max_right:
                left_index += 1
                water = max_left - height[left_index]

            else:
                right_index -= 1
                water = max_right - height[right_index]


            water = max(0, water)
            res += water

            max_left = max(max_left, height[left_index])
            max_right = max(max_right, height[right_index])

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


