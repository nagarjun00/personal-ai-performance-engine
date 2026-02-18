from datetime import date
from core.models.coding_session import CodingSession
from core.scoring.skill_scoring import SkillScorer


def test_basic_delta_calculation():
    session = CodingSession(
        skill_name="Python",
        difficulty=2,
        correctness=1,
        retries=1,
        ideal_time=60,
        actual_time=60,
        session_date=date.today()
    )

    delta = SkillScorer.calculate_delta(session)

    # D=2, C=1, T=1.0, R=0.2
    # (2*8*1*1) - (5*0.2)
    # 16 - 1 = 15
    assert round(delta, 2) == 15


def test_retry_clamp():
    session = CodingSession(
        skill_name="Python",
        difficulty=2,
        correctness=1,
        retries=10,  # 10*0.2=2 → clamp to 1
        ideal_time=60,
        actual_time=60,
        session_date=date.today()
    )

    delta = SkillScorer.calculate_delta(session)

    # (16) - (5*1)
    # 16 - 5 = 11
    assert round(delta, 2) == 11


def test_time_clamp():
    session = CodingSession(
        skill_name="Python",
        difficulty=1,
        correctness=1,
        retries=0,
        ideal_time=60,
        actual_time=200,  # T = 0.3 → clamp to 0.5
        session_date=date.today()
    )

    delta = SkillScorer.calculate_delta(session)

    # (1*8*1*0.5) - 0
    # 4
    assert round(delta, 2) == 4
