from abc import ABC, abstractmethod

class ArrivalClientInterface(ABC):

    @abstractmethod
    def create_request(self, distance, speed):
        pass