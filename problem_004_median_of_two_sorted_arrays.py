from typing import List
from math import inf


class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:

        if len(a) > len(b):
            a, b = b, a

        m, n = len(a), len(b)
        low, high = 0, m
        half_elements = (n + m + 1) // 2

        while low <= high:
            i = (low + high + 1) // 2
            j = half_elements - i

            max_left_a = a[i - 1] if i > 0 else -inf
            min_right_a = a[i] if i < len(a) else inf

            max_left_b = b[j - 1] if j > 0 else -inf
            min_right_b = b[j] if j < len(b) else inf

            if max_left_a <= min_right_b and \
               max_left_b <= min_right_a:

                # even number of elements
                if (m + n) % 2 == 0:
                    return (max(max_left_a, max_left_b) +
                            min(min_right_a, min_right_b)) / 2

                # odd number of elements
                else:
                    return max(max_left_a, max_left_b)

            elif max_left_a > min_right_b:
                high = i - 1

            else:
                low = i + 1
