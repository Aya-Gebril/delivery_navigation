from delivery_navigation.interfaces.arrival_estimator import ArrivalEstimator

class ArrivalTimeService(ArrivalEstimator):
    def estimate(self, distance, speed):
        if speed <= 0:
            return 0.0

        return (distance / speed)