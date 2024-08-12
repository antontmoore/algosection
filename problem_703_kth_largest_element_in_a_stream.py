from heapq import heapify, nsmallest, heappush, heappop, nlargest
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapify(nums)
        self.nums = nums
        while len(self.nums) > k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        heappush(self.nums, val)
        while len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]


if __name__ == "__main__":
    kl = KthLargest(3, [4, 5, 8, 2])
    res = [None]
    res.append(kl.add(3))
    res.append(kl.add(5))
    res.append(kl.add(10))
    res.append(kl.add(9))
    res.append(kl.add(4))
    print(res)