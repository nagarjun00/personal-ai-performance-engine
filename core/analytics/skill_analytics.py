import statistics


class SkillAnalytics:

    def __init__(self, repository, scorer):
        self.repository = repository
        self.scorer = scorer

    # --------------------
    # Basic Metrics
    # --------------------

    def total_sessions(self, skill_name: str) -> int:
        sessions = self.repository.get_sessions_by_skill(skill_name)
        return len(sessions)

    def total_time_invested(self, skill_name: str) -> float:
        sessions = self.repository.get_sessions_by_skill(skill_name)
        return sum(session.actual_time for session in sessions)

    def average_delta(self, skill_name: str) -> float:
        sessions = self.repository.get_sessions_by_skill(skill_name)

        if not sessions:
            return 0.0

        deltas = [self.scorer.calculate_delta(s) for s in sessions]
        return sum(deltas) / len(deltas)

    # --------------------
    # Advanced Metrics
    # --------------------

    def consistency_score(self, skill_name: str) -> float:
        sessions = self.repository.get_sessions_by_skill(skill_name)

        if len(sessions) < 2:
            return 0.0

        sessions_sorted = sorted(sessions, key=lambda s: s.session_date)

        first = sessions_sorted[0].session_date
        last = sessions_sorted[-1].session_date

        active_span = (last - first).days or 1

        return len(sessions) / active_span

    def recent_average_delta(self, skill_name: str, last_n: int = 3) -> float:
        sessions = self.repository.get_sessions_by_skill(skill_name)

        if not sessions:
            return 0.0

        sessions_sorted = sorted(sessions, key=lambda s: s.session_date)

        recent = sessions_sorted[-last_n:]
        deltas = [self.scorer.calculate_delta(s) for s in recent]

        return sum(deltas) / len(deltas)

    def momentum_score(self, skill_name: str, last_n: int = 3) -> float:
        overall = self.average_delta(skill_name)
        recent = self.recent_average_delta(skill_name, last_n)

        return recent - overall

    def volatility(self, skill_name: str) -> float:
        sessions = self.repository.get_sessions_by_skill(skill_name)

        if len(sessions) < 2:
            return 0.0

        deltas = [self.scorer.calculate_delta(s) for s in sessions]

        return statistics.stdev(deltas)
