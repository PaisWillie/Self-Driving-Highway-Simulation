from random import random
import time
from typing import List

from Highway.highway import Highway
from Highway.self_driving_lane import SelfDrivingLane
from Highway.shared_lane import SharedLane
from Vehicles.desires import Desire
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

            for i in range(len(self.highway.lanes)):
                for vehicle in self.highway.lanes[i].road:
                    # Check if self-driven vehicle is not in self-driving lane, then set desire to LANE_CHANGE_LEFT
                    if type(vehicle) is SelfDrivenVehicle and type(self.highway.lanes[i]) is not SelfDrivingLane and i != 0:
                        self.highway.lanes[i].lane_change(
                            vehicle, self.highway.lanes[i-1])

                    # Check if human-driven vehicle is not in shared lane, then set desire to LANE_CHANGE_RIGHT
                    elif type(vehicle) is HumanDrivenVehicle and type(self.highway.lanes[i]) is not SharedLane and i != len(self.highway.lanes)-1:
                        self.highway.lanes[i].lane_change(
                            vehicle, self.highway.lanes[i+1])

            num_self_driving_lanes = 0

            for lane in self.highway.lanes:
                if type(lane) is SelfDrivingLane:
                    num_self_driving_lanes += 1

            ratio = self.highway.get_ratio_self_driven_to_shared()
            # print("ratio: " + str(ratio))

            if (ratio > ((num_self_driving_lanes + 1)/len(self.highway.lanes))):
                self.highway.increase_self_driving_lanes()
            elif (ratio < (num_self_driving_lanes/len(self.highway.lanes))):
                self.highway.increase_shared_lanes()

            self.highway.print()

            # TODO:
            # Check ratio of vehcile types
            # Convert lanes depending on ratio
            # For each driver, determine desire
            # For each driver, if desire is to change lane, change lane
            # For each driver, if desire is to cruise, cruise

            self.current_step += 1
            time.sleep(0.35)

    def execute_time_step(self) -> None:
        # TODO: Move drivers
        for lane in self.highway.lanes:
            for i in range(lane.length - 1, -1, -1):
                if (lane.road[i] is not None):
                    lane.road[i].drive(lane)

    def gen_new_drivers(self) -> None:
        for lane in self.highway.lanes:

            random_chance = random()

            if type(lane) is SelfDrivingLane and \
                    random_chance < self.chance_gen_self_driven_vehicle and \
                    lane.can_generate_vehicle(self.self_driven_vehicle_safe_follow_distance):
                lane.set_vehicle(0,
                                 SelfDrivenVehicle(lane.speed_limit,
                                                   self.self_driven_vehicle_safe_follow_distance,
                                                   self.self_driven_vehicle_acceleration))
            elif type(lane) is SharedLane:

                # TODO: Priority of vehicle type depending on chance?
                if random_chance < self.chance_gen_self_driven_vehicle and \
                        lane.can_generate_vehicle(self.self_driven_vehicle_safe_follow_distance):
                    lane.set_vehicle(0,
                                     SelfDrivenVehicle(lane.speed_limit,
                                                       self.self_driven_vehicle_safe_follow_distance,
                                                       self.self_driven_vehicle_acceleration))

                elif random_chance < self.chance_gen_human_driven_vehicle and \
                        lane.can_generate_vehicle(self.human_driven_vehicle_safe_follow_distance):
                    lane.set_vehicle(0,
                                     HumanDrivenVehicle(lane.speed_limit,
                                                        self.human_driven_vehicle_safe_follow_distance,
                                                        self.human_driven_vehicle_acceleration))

    # def average_time(self):
    #     pass
