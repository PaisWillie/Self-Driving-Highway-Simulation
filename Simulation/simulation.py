from random import random
import time
from typing import List

from Highway.highway import Highway
from Highway.self_driving_lane import SelfDrivingLane
from Highway.shared_lane import SharedLane
from Vehicles.human_driven_vehicle import HumanDrivenVehicle
from Vehicles.self_driven_vehicle import SelfDrivenVehicle


class Simulation:

    highway: Highway
    time_steps: int
    current_step: int

    chance_gen_self_driven_vehicle: int
    chance_gen_human_driven_vehicle: int
    # TODO: Maybe have chance for self-driven vehicle on shared lane?

    self_driven_vehicle_safe_follow_distance: int
    human_driven_vehicle_safe_follow_distance: int

    self_driven_vehicle_acceleration: int
    human_driven_vehicle_acceleration: int

    def __init__(self, length: int,
                 num_self_driving_lanes: int,
                 num_shared_lanes: int,
                 self_driving_speed_limit: int,
                 shared_speed_limit: int,
                 time_steps: int,
                 entry_points: List[int],
                 chance_gen_self_driven_vehicle: int,
                 chance_gen_human_driven_vehicle: int,
                 self_driven_vehicle_safe_follow_distance: int,
                 human_driven_vehicle_safe_follow_distance: int,
                 self_driven_vehicle_acceleration: int,
                 human_driven_vehicle_acceleration: int
                 ) -> None:
        self.highway = Highway(length,
                               num_self_driving_lanes,
                               num_shared_lanes,
                               self_driving_speed_limit,
                               shared_speed_limit,
                               entry_points)
        self.time_steps = time_steps
        self.current_step = 0

        self.chance_gen_self_driven_vehicle = chance_gen_self_driven_vehicle
        self.chance_gen_human_driven_vehicle = chance_gen_human_driven_vehicle

        self.self_driven_vehicle_safe_follow_distance = self_driven_vehicle_safe_follow_distance
        self.human_driven_vehicle_safe_follow_distance = human_driven_vehicle_safe_follow_distance

        self.self_driven_vehicle_acceleration = self_driven_vehicle_acceleration
        self.human_driven_vehicle_acceleration = human_driven_vehicle_acceleration

    def run(self) -> None:
        while self.current_step < self.time_steps:
            self.execute_time_step()
            self.gen_new_drivers()
            self.highway.print()

            # TODO:
            # Check ratio of vehcile types
            # Convert lanes depending on ratio
            # For each driver, determine desire
            # For each driver, if desire is to change lane, change lane
            # For each driver, if desire is to cruise, cruise

            self.current_step += 1
            time.sleep(0.5)

    def execute_time_step(self) -> None:
        pass

    def gen_new_drivers(self) -> None:
        # TODO: Generate new drivers based on random chance
        random_chance = random()

        for lane in self.highway.lanes:
            if type(lane) is SelfDrivingLane and random_chance < self.chance_gen_self_driven_vehicle:
                # TODO: Only generate vehicle at speed_limit if safe follow distance is statisfied
                lane.set_vehicle(0,
                                 SelfDrivenVehicle(lane.speed_limit,
                                                   self.self_driven_vehicle_safe_follow_distance,
                                                   self.self_driven_vehicle_acceleration))
            elif type(lane) is SharedLane:
                if random_chance < self.chance_gen_self_driven_vehicle:
                    lane.set_vehicle(0,
                                     SelfDrivenVehicle(lane.speed_limit,
                                                       self.self_driven_vehicle_safe_follow_distance,
                                                       self.self_driven_vehicle_acceleration))
                    if random_chance < self.chance_gen_human_driven_vehicle:
                        lane.set_vehicle(0,
                                     HumanDrivenVehicle(lane.speed_limit,
                                                       self.human_driven_vehicle_safe_follow_distance,
                                                       self.human_driven_vehicle_acceleration))

    # def average_time(self):
    #     pass
