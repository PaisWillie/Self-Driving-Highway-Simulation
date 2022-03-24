from typing import List
from lane import Lane

class Highway:

    lanes: List[Lane]

    def __init__(self) -> None:
        pass   
        
    def lane_position(self, curr_lane: Lane):
        # Check if it works by reference
        return self.lanes.index(curr_lane)

    def can_lane_change(self, position: int, lane: Lane, direction: str) -> bool:
        pass