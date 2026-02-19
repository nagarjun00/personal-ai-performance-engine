from datetime import timedelta
from core.models.coding_session import CodingSession


class MultiDaySimulator:

    def __init__(self, engine):
        self.engine = engine

    def run(
        self,
        skill_name: str,
        start_date,
        number_of_days: int,
        ideal_time: float = 60,
    ):
        for day in range(number_of_days):

            current_date = start_date + timedelta(days=day)

            # Deterministic patterns
            difficulty = (day % 3) + 1
            correctness = 1 if day % 3 != 2 else 0
            retries = day % 3

            # Simulate slight improvement in speed
            actual_time = max(30, ideal_time - (day * 1.5))

            session = CodingSession(
                skill_name=skill_name,
                difficulty=difficulty,
                correctness=correctness,
                retries=retries,
                ideal_time=ideal_time,
                actual_time=actual_time,
                session_date=current_date,
            )

            self.engine.process_session(session)

            # Apply daily decay after session
            self.engine.apply_decay_to_all(current_date)
