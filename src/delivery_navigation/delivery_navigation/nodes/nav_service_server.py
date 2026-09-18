import rclpy
from rclpy.node import Node
from robot_interfaces.srv import EstimateArrivalTime
from delivery_navigation.services.arrival_time_service import ArrivalTimeService

class NavServiceServer(Node):
    def __init__(self):
        super().__init__('nav_service_server')
        self.service = ArrivalTimeService()
        self.server = self.create_service(EstimateArrivalTime, 'estimate_arrival_time', self.calculate_eta)

    def calculate_eta(self, request, response):
        response.seconds_remaining = self.service.estimate(request.distance_remaining, request.speed)
        return response

def main():
    rclpy.init()
    node = NavServiceServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()