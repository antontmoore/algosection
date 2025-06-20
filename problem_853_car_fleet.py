from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))

        times = [(target - p) / s for p, s in cars]
        ans = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]:
                ans += 1
            else:
                times[-1] = lead
        return ans + bool(times)


if __name__ == "__main__":
    s = Solution()
    res = s.carFleet(target=100, position=[0, 2, 4], speed=[4, 2, 1])
    print(res)
