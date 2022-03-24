from abc import ABC, abstractmethod
from typing import List

from Vehicles.vehicle import Vehicle

class Lane(ABC):

    road: List[int] 
    length: int
    speed_limit: int

    def __init__(self, length, speed_limit) -> None:
        self.road = []
        self.length = length
        self.speed_limit = speed_limit
        for _ in range(length):
            self.road[0].append(None)

    @abstractmethod
    def can_move_forward(self, vehicle: Vehicle) -> bool:
        pass

    @abstractmethod
    def can_lane_change(self, position: int) -> bool:
        pass

    @abstractmethod
    def get(self, lane, index) -> int:
        pass

    @abstractmethod
    def set(self, lane, index, value):
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