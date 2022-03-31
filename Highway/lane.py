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
        self.set_vehicle(self.get_vehicle_position(vehicle), None)
        self.set_vehicle(new_position, vehicle)

    # @abstractmethod
    # def can_lane_change(self, position: int, new_lane) -> bool:
    #     pass
    # TODO: Highway class' method?
    
    @abstractmethod
    def can_generate_vehicle(self, safe_follow: int) -> bool:
        pass

    @abstractmethod
    def safe_distance_within(self, lane, index, k):
        pass

    @abstractmethod
    def safe_right_lane_change(self, i):
        pass

    @abstractmethod
    def safe_left_lane_change(self, i):
        pass

    @abstractmethod
    def print(self):
        pass