from abc import ABC, abstractmethod
from typing import List

from Highway.lane import Lane

class Vehicle(ABC):

    speed: int
    desire: str
    arrive_time: int
    safe_follow: int

    def __init__(self, speed: int, desire: str, arrive_time: int, safe_follow: int) -> None:
        self.arrive_time = arrive_time
        self.speed = speed
        self.desire = desire
        self.safe_follow = safe_follow

    def accelerate(self, acceleration: int) -> None:
        if acceleration < 0 and self.speed > 0:
            if self.speed + acceleration > 0:
                self.speed += acceleration
            else:
                self.speed = 0
        else:
            self.speed += acceleration

    def drive(self, lane: Lane) -> None:
        if lane.can_move_forward(self):
            self.position += 1

    # Returns true if the vehicle successfully changes lanes
    @abstractmethod
    def change_lane(self) -> bool:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass