import rclpy
from rclpy.node import Node
from robot_interfaces.msg import RobotStatus
from delivery_navigation.services.status_service import StatusService

class NavSubscriber(Node):
    def __init__(self):
        super().__init__('nav_subscriber')
        self.service = StatusService()
        self.subscription = self.create_subscription(RobotStatus, 'robot_status', self.status_callback, 10)

    def status_callback(self, msg):
        self.get_logger().info(self.service.process_status(msg))

def main():
    rclpy.init()
    node = NavSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()