from abc import ABC, abstractmethod

class StatusInterface(ABC):

    @abstractmethod
    def process_status(self, msg):
        pass