from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting_time = 0
        has_to_work_until = 0
        for c in customers:
            current_time = c[0]
            if has_to_work_until < current_time:
                has_to_work_until = current_time
            has_to_work_until += c[1]
            waiting_time += has_to_work_until - current_time
        return waiting_time / len(customers)
