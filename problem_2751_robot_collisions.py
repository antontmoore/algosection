from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:

        index_by_pos = {p: i for i, p in enumerate(positions)}

        stack = []
        for pos in sorted(positions):
            i = index_by_pos[pos]

            if directions[i] == 'L':
                while stack and healths[i] > 0:
                    left_i = stack.pop()
                    if healths[i] == healths[left_i]:
                        healths[i] = 0
                        healths[left_i] = 0
                    elif healths[i] > healths[left_i]:
                        healths[i] -= 1
                        healths[left_i] = 0
                    else:
                        healths[left_i] -= 1
                        healths[i] = 0
                        stack.append(left_i)
            else:
                stack.append(i)

        return [h for h in healths if h > 0]


if __name__ == "__main__":
    s = Solution()
    res = s.survivedRobotsHealths([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], "RRRRR")
    # res = s.survivedRobotsHealths([4, 47], [15, 24], "RR")
    print(res)
