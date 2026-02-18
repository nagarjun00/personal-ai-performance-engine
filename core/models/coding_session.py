from datetime import date


class CodingSession:
    def __init__(
        self,
        skill_name: str,
        difficulty: int,
        correctness: int,
        retries: int,
        ideal_time: float,
        actual_time: float,
        session_date: date,
    ):
        self.skill_name = skill_name
        self.difficulty = difficulty
        self.correctness = correctness
        self.retries = retries
        self.ideal_time = ideal_time
        self.actual_time = actual_time
        self.session_date = session_date
