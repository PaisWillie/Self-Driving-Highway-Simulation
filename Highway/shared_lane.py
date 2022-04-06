from Highway.lane import Lane


class SharedLane(Lane):

    def __init__(self, length, speed_limit) -> None:
        super().__init__(length, speed_limit)
