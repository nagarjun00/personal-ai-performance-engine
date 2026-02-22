from datetime import timedelta
from core.models.coding_session import CodingSession


class StrategicSimulator:

    def __init__(self, engine):
        self.engine = engine

    def run(
        self,
        start_date,
        number_of_days: int,
        ideal_time: float = 60,
    ):
        for day in range(number_of_days):

            current_date = start_date + timedelta(days=day)

            # 1️⃣ Apply decay first
            self.engine.apply_decay_to_all(current_date)

            # 2️⃣ Get highest priority skill
            focus_skill = self.engine.get_daily_focus()

            if focus_skill is None:
                continue

            # 3️⃣ Deterministic session parameters
            difficulty = (day % 3) + 1
            correctness = 1 if day % 3 != 2 else 0
            retries = day % 3
            actual_time = max(30, ideal_time - (day * 1.2))

            session = CodingSession(
                skill_name=focus_skill.name,
                difficulty=difficulty,
                correctness=correctness,
                retries=retries,
                ideal_time=ideal_time,
                actual_time=actual_time,
                session_date=current_date,
            )

            self.engine.process_session(session)