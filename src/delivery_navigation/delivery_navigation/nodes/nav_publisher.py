import rclpy
from rclpy.node import Node
from robot_interfaces.msg import RobotStatus
from delivery_navigation.services.navigation_service import NavigationService

class NavPublisher(Node):
    def __init__(self):
        super().__init__('nav_publisher')
        self.publisher = self.create_publisher(RobotStatus, 'robot_status', 10)
        self.service = NavigationService()
        self.timer = self.create_timer(1.0, self.publish_status)

    def publish_status(self):
        self.publisher.publish(self.service.get_next_status())

def main():
    rclpy.init()
    rclpy.spin(NavPublisher())
    rclpy.shutdown()