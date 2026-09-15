from abc import ABC, abstractmethod

class NavigationInterface(ABC):

    @abstractmethod
    def get_next_status(self):
        pass