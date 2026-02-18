from datetime import date
from typing import Optional


class Skill:
    def __init__(
        self,
        name: str,
        strength: float = 0.0,
        role_weight: float = 1.0,
        last_practiced: Optional[date] = None,
    ):
        self.name = name
        self.strength = max(0, min(100, strength))
        self.role_weight = role_weight
        self.last_practiced = last_practiced

    def update_strength(self, delta: float) -> None:
        self.strength = max(0, min(100, self.strength + delta))

    def apply_decay(self, multiplier: float) -> None:
        self.strength = max(0, min(100, self.strength * multiplier))
