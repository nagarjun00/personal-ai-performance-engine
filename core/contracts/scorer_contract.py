from abc import ABC, abstractmethod


class BaseScorer(ABC):

    @abstractmethod
    def calculate_delta(self, session) -> float:
        pass
