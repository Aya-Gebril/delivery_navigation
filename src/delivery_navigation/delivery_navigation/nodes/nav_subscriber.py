import rclpy
from rclpy.node import Node
from robot_interfaces.msg import RobotStatus
from robot_interfaces.srv import EstimateArrivalTime
from delivery_navigation.services.arrival_client_service import (ArrivalClientService)
from delivery_navigation.services.status_service import StatusService

class NavSubscriber(Node):
    def __init__(self):
        super().__init__('nav_subscriber')
        self.service = StatusService()
        self.arrival_service = ArrivalClientService()
        self.client = self.create_client(EstimateArrivalTime, 'estimate_arrival_time')
        self.subscription = self.create_subscription(RobotStatus, 'robot_status', self.status_callback, 10)

    def status_callback(self, msg):
        self.get_logger().info(self.service.process_status(msg))
        request = EstimateArrivalTime.Request()
        distance, speed = self.arrival_service.create_request(msg.distance_remaining, msg.speed)
        request.distance_remaining = distance
        request.speed = speed
        if not self.client.service_is_ready():
            self.get_logger().warn('Arrival time service is not available.')
            return
        future = self.client.call_async(request)
        future.add_done_callback(self.arrival_response_callback)
        
    def arrival_response_callback(self, future):
        try:
            response = future.result()
            self.get_logger().info(f'Estimated arrival time: {response.minutes_remaining:.2f} minutes')
        except Exception as e:
            self.get_logger().error(f'Service call failed: {e}')

def main():
    rclpy.init()
    node = NavSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()

if __name__ == '__main__':
    main()