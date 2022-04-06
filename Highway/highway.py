from multiprocessing.spawn import old_main_modules
from Vehicles.human_driven_vehicle import HumanDrivenVehicle
from Vehicles.self_driven_vehicle import SelfDrivenVehicle

from Highway.self_driving_lane import SelfDrivingLane
from Highway.shared_lane import SharedLane
from typing import List
from Highway.lane import Lane


class Highway:

    lanes: List[Lane]
    entry_point: List[int]
    num_self_driving_lanes: int
    num_shared_lanes: int
    self_driving_speed_limit: int
    shared_speed_limit: int
    length: int

    def __init__(self,
                 length: int,
                 num_self_driving_lanes: int,
                 num_shared_lanes: int,
                 self_driving_speed_limit: int,
                 shared_speed_limit: int,
                 entry_points: List[int]
                 ) -> None:
        self.length = length
        self.num_self_driving_lanes = num_self_driving_lanes
        self.num_shared_lanes = num_shared_lanes
        self.shared_speed_limit = shared_speed_limit
        self.self_driving_speed_limit = self_driving_speed_limit
        self.lanes = []
        for _ in range(num_self_driving_lanes):
            self.lanes.append(SelfDrivingLane(
                length, self_driving_speed_limit))
        for _ in range(num_shared_lanes):
            self.lanes.append(SharedLane(length, shared_speed_limit))

        self.entry_point = entry_points

    def lane_position(self, curr_lane: Lane):
        # Check if it works by reference
        return self.lanes.index(curr_lane)

    def can_lane_change(self, position: int, lane: Lane) -> bool:
        pass

    def increase_self_driving_lanes(self) -> None:
        if self.num_shared_lanes > 1:

            old_lane = self.lanes[self.num_self_driving_lanes]

            self.lanes[self.num_self_driving_lanes] = SelfDrivingLane(
                self.length, self.self_driving_speed_limit)

            # Move vehicles from shared lane to self-driving lane
            for i in range(self.length):
                self.lanes[self.num_self_driving_lanes].set_vehicle(
                    i, old_lane.get_vehicle(i))

            self.num_shared_lanes -= 1
            self.num_self_driving_lanes += 1

    def increase_shared_lanes(self) -> None:
        if self.num_self_driving_lanes > 1:

            old_lane = self.lanes[self.num_self_driving_lanes - 1]

            self.lanes[self.num_self_driving_lanes -
                       1] = SharedLane(self.length, self.shared_speed_limit)

            # Move vehicles from self-driving lane to shared lane
            for i in range(self.length):
                self.lanes[self.num_self_driving_lanes -
                           1].set_vehicle(i, old_lane.get_vehicle(i))

            self.num_self_driving_lanes -= 1
            self.num_shared_lanes += 1

    def get_ratio_self_driven_to_shared(self) -> float:

        num_human_driven = 0
        num_self_driven = 0

        for lane in self.lanes:
            for vehicle in lane.road:
                if type(vehicle) is HumanDrivenVehicle:
                    num_human_driven += 1
                elif type(vehicle) is SelfDrivenVehicle:
                    num_self_driven += 1

        if (num_self_driven + num_human_driven) == 0:
            return 0

        return num_self_driven / (num_self_driven + num_human_driven)

    def print(self) -> None:
        for i in range(len(self.lanes)):
            if type(self.lanes[i]) is SelfDrivingLane:
                print("Self-driving lane: \t", end="")
                for j in range(self.length):
                    vehicle = self.lanes[i].get_vehicle(j)
                    if type(vehicle) is SelfDrivenVehicle:
                        print("S ", end="")
                    elif type(vehicle) is HumanDrivenVehicle:
                        print("H ", end="")
                    else:
                        print("- ", end="")
                print("")
            if type(self.lanes[i]) is SharedLane:
                print("Shared lane: \t\t", end="")
                for j in range(self.length):
                    vehicle = self.lanes[i].get_vehicle(j)
                    if type(vehicle) is SelfDrivenVehicle:
                        print("S ", end="")
                    elif type(vehicle) is HumanDrivenVehicle:
                        print("H ", end="")
                    else:
                        print("- ", end="")
                print("")

        # Print entry-points
        # print("\t\t\t", end="")
        # for i in range(self.length):
        #     if i in self.entry_point:
        #         print("E ", end="")
        #     else:
        #         print("  ", end="")

        print("\n")
