from abc import ABC, abstractmethod
from datetime import date


class BaseDecayPolicy(ABC):

    @abstractmethod
    def compute_decay_multiplier(
        self,
        last_practiced: date,
        current_date: date
    ) -> float:
        pass
