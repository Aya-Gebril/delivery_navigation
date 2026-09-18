from delivery_navigation.interfaces.arrival_client_interface import (ArrivalClientInterface)

class ArrivalClientService(ArrivalClientInterface):
    def create_request(self, distance, speed):
        return distance, speed