from abc import ABC, abstractmethod
from typing import List

from Vehicles.vehicle import Vehicle


class Lane(ABC):

    road: List[Vehicle]
    length: int
    speed_limit: int

    def __init__(self, length, speed_limit) -> None:
        self.road = []
        self.length = length
        self.speed_limit = speed_limit
        for _ in range(length):
            self.road.append(None)

    def drive_all_vehicles(self) -> None:
        for position in range(0, self.length):
            self.road[position].drive(self)

    def get_vehicle_position(self, vehicle: Vehicle) -> int:
        for position in range(0, self.length):
            if self.road[position] == vehicle:
                return position

    def get_vehicle(self, index) -> Vehicle:
        return self.road[index]

    def set_vehicle(self, index, vehicle: Vehicle) -> None:
        self.road[index] = vehicle

    def move_vehicle(self, vehicle: Vehicle, new_position: int) -> None:
        if new_position < self.length:
            self.set_vehicle(new_position, vehicle)
        self.set_vehicle(self.get_vehicle_position(vehicle), None)

    def can_generate_vehicle(self, safe_follow: int) -> bool:
        for position in range(0, safe_follow):
            if self.road[position] is not None:
                return False
        return True

    def lane_change(self, vehicle: Vehicle, new_lane):
        position = self.get_vehicle_position(vehicle)
        if new_lane.get_vehicle(position) is None:
            new_lane.set_vehicle(position, vehicle)
            self.set_vehicle(position, None)
            vehicle.speed = new_lane.speed_limit
        else:
            # print("decelerating because cannot lane change")
            vehicle.accelerate('-', self.speed_limit)
