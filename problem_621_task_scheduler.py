from typing import List
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # in maxheap we store tasks that ARE AVAILABLE to execute right now
        # in queue we store tasks that are waiting their idle time and cannot be executed right now
        counter = {}
        for t in tasks:
            counter[t] = counter.get(t, 0) + 1

        max_heap = [-cnt for cnt in counter.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()  # pairs of [-cnt, idle_time_end]
        while max_heap or q:
            time += 1
            if max_heap:
                # execute the task
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                # now we can put this task into maxheap again, cause it's idle time has passed
                heapq.heappush(max_heap, q.popleft()[0])

        return time


if __name__ == "__main__":
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    s = Solution()
    res = s.leastInterval(tasks, n)
    print(res)