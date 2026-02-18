from abc import ABC, abstractmethod


class BasePriorityCalculator(ABC):

    @abstractmethod
    def calculate_priority(self, skill) -> float:
        pass
