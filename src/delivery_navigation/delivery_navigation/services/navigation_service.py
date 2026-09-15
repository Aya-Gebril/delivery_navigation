import random
from robot_interfaces.msg import RobotStatus
from delivery_navigation.interfaces.navigation_interface import (NavigationInterface)

class NavigationService(NavigationInterface):
    def __init__(self):
        self.distance = 20.0
        self.speed = 2.0

    def get_next_status(self):
        msg = RobotStatus()
        msg.distance_remaining = self.distance
        msg.speed = self.speed
        msg.obstacle_detected = random.choice([False, False, False, True])
        self.distance = max(0.0, self.distance - self.speed)

        return msg