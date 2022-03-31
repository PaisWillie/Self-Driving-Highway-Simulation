import load_config
from Highway.lane import Lane

class SelfDrivingLane(Lane):

    def __init__(self, length, speed_limit) -> None:
        super().__init__(length, speed_limit)

    def safe_distance_within(self, lane, index, k):
        pass

    def safe_right_lane_change(self, i):
        pass

    def safe_left_lane_change(self, i):
        pass

    def print(self):
        pass