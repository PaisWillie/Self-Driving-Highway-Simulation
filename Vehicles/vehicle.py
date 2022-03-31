from abc import ABC, abstractmethod

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
        if self.can_drive_forward(lane):
            lane.move_vehicle(self, self.get_position(lane) + self.speed + self.safe_follow)

    # Returns true if the vehicle successfully changes lanes
    @abstractmethod
    def change_lane(self) -> bool:
        pass

    @abstractmethod
    def can_drive_forward(self, lane) -> bool:
        position = lane.get_vehicle_position(self)
        if lane.get_vehicle(position + self.speed + self.safe_follow) is None:
            return True

    @abstractmethod
    def __str__(self) -> str:
        pass
