## TODO List
# - Car speed & accerleration
# - Lane change only into accessible lanes
# - Abstract vehicle class
# - Changing number of self-driving vehicle only lanes
# - Highway abstract class (different speed limit)
# - Ratio of self-driven to human-driven vehicles
# - Multiple entry/exit points
# - Multiple lanes
# - Different desired speed target per driver
# - Intention to merge off of self-driving lane if current lane converted

# TODO: Self-driven vehicle class
class SelfDrivingVehicle:
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def drive(self):
        print(f"{self.name} is driving at {self.speed} mph")

    def stop(self):
        print(f"{self.name} is stopping")

    def change_speed(self, new_speed):
        self.speed = new_speed
        print(f"{self.name} is now driving at {self.speed} mph")

class HumanDrivingVehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def drive(self):
        print(f"{self.name} is driving at {self.speed} mph")

    def change_speed(self, new_speed):
        self.speed = new_speed
        print(f"{self.name} is now driving at {self.speed} mph")

    # Set the acceleration of the vehicle
    def accelerate(self, acceleration):
        self.speed += acceleration
        print(f"{self.name} is now driving at {self.speed} mph")

    # Set the deceleration of the vehicle
    # If the vehicle speed is zero, the deceleration is ignored
    def decelerate(self, deceleration):
        if self.speed > 0:
            self.speed -= deceleration
            print(f"{self.name} is now driving at {self.speed} mph")
        else:
            print(f"{self.name} is already stopped")

    # Set the vehicle to stop
    def stop(self):
        self.speed = 0
        print(f"{self.name} is now stopped")
    

# TODO: Human-driven vehicle class

# TODO: Highway class

# TODO: Lane abstract class


if __name__ == '__main__':
    pass