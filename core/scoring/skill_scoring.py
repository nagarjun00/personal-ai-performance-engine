from core.contracts.scorer_contract import BaseScorer


class SkillScorer(BaseScorer):

    @staticmethod
    def calculate_delta(session) -> float:
        D = session.difficulty
        C = session.correctness

        R = session.retries * 0.2
        R = max(0, min(1, R))

        T_raw = session.ideal_time / session.actual_time
        T = max(0.5, min(1.2, T_raw))

        delta = (D * 8 * C * T) - (5 * R)
        return delta
