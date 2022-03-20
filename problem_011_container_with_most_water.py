from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1

        max_area = 0
        while right > left:
            area = (right - left) * min(height[right], height[left])
            if area > max_area:
                max_area = area

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == "__main__":
    sol_class = Solution()
    ans = sol_class.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(ans)
