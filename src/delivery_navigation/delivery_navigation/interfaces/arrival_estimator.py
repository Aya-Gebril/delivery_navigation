from abc import ABC, abstractmethod

class ArrivalEstimator(ABC):

    @abstractmethod
    def estimate(self, distance, speed):
        pass