from abc import ABC, abstractmethod
from os import access

from Vehicles.desires import Desire


class Vehicle(ABC):

    speed: int
    desire: str
    arrive_time: int
    safe_follow: int
    acceleration: int

    def __init__(self,
                 speed: int,
                 safe_follow: int,
                 acceleration: int
                 ) -> None:
        self.arrive_time = 0
        self.speed = speed
        self.desire = Desire.CRUISE
        self.safe_follow = safe_follow
        self.acceleration = acceleration

    def accelerate(self, intention: str, speed_limit: int) -> None:

        if intention != '-' and intention != '+':
            raise ValueError('Invalid intention')

        elif intention == '-' and self.speed > 0:
            if self.speed - self.acceleration > 0:
                self.speed -= self.acceleration
            else:
                self.speed = 0

        elif intention == '+' and self.speed + self.acceleration <= speed_limit:
            self.speed += self.acceleration

    def drive(self, lane) -> None:
        # TODO: Test this

        # TODO: If desire is CHANGE_LANE_LEFT or CHANGE_LANE_RIGHT, change lane if possible, else drive forward
        # TODO: If desire is CRUISE, drive forward if possible, else change lane if possible

        position = lane.get_vehicle_position(self)

        # Checks if vehicle needs to slow down
        if (not self.can_drive_forward(lane)) and self.speed > 0:
            while (not self.can_drive_forward(lane) and self.speed > 0):
                self.accelerate('-', lane.speed_limit)

        # Checks if vehicle can accelerate
        elif (self.speed < lane.speed_limit):
            self.accelerate('+', lane.speed_limit)
            if not self.can_drive_forward(lane):
                self.accelerate('-', lane.speed_limit)

        lane.move_vehicle(self, position + self.speed)

    def can_drive_forward(self, lane) -> bool:
        position = lane.get_vehicle_position(self)
        for i in range(position + 1, position + self.speed + self.safe_follow):
            if i < lane.length and lane.get_vehicle(i) is not None:
                return False
        return True
