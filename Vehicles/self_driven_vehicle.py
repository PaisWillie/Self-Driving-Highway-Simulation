from Vehicles.vehicle import Vehicle


class SelfDrivenVehicle(Vehicle):

    def __init__(self,
                 speed: int,
                 safe_follow: int,
                 acceleration: int
                 ) -> None:
        super().__init__(speed,
                         safe_follow,
                         acceleration)

    def change_lane(self) -> bool:
        return

    def __str__(self) -> str:
        return
