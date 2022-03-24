from Vehicles.vehicle import Vehicle

class SelfDrivenVehicle(Vehicle):

    def __init__(self, speed: int, desire: str, arrive_time: int, safe_follow: int) -> None:
        super().__init__(speed, desire, arrive_time, safe_follow)

    