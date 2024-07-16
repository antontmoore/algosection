from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(list(zip(position, speed)), key=lambda x: x[0])

        number_of_fleets = 1
        last_car = ps.pop()
        current_fleet_time_at_target = (target - last_car[0]) / last_car[1]
        for car in ps[::-1]:
            time_at_target = (target - car[0]) / car[1]
            if time_at_target > current_fleet_time_at_target:
                number_of_fleets += 1
                current_fleet_time_at_target = time_at_target

        return number_of_fleets
