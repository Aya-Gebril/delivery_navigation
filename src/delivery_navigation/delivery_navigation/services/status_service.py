from delivery_navigation.interfaces.status_interface import StatusInterface

class StatusService(StatusInterface):
    def process_status(self, msg):
        if msg.obstacle_detected:
            return f'WARNING: Obstacle detected! Distance: {msg.distance_remaining:.1f}m'

        return f'Distance: {msg.distance_remaining:.1f}m | Speed: {msg.speed:.1f}m/s'