from datetime import date

from core.models.skill import Skill
from core.models.coding_session import CodingSession
from core.engine.skill_engine import SkillEngine

from repository.in_memory_repository import InMemorySkillRepository

from core.scoring.skill_scoring import SkillScorer
from core.decay.decay_policy import DecayPolicy
from core.prioritization.priority_calculator import PriorityCalculator


def main():
    repo = InMemorySkillRepository()

    # Create skills
    python_skill = Skill(name="Python", strength=50, role_weight=1.5)
    algo_skill = Skill(name="Algorithms", strength=30, role_weight=2.0)

    repo.save_skill(python_skill)
    repo.save_skill(algo_skill)

    # Inject dependencies (Strategy Injection)
    engine = SkillEngine(
        repository=repo,
        scorer=SkillScorer(),
        decay_policy=DecayPolicy(),
        priority_calculator=PriorityCalculator(),
    )

    # Simulate session
    session = CodingSession(
        skill_name="Algorithms",
        difficulty=3,
        correctness=1,
        retries=1,
        ideal_time=60,
        actual_time=50,
        session_date=date.today(),
    )

    engine.process_session(session)

    #For Verification
    print("\nSession History for Algorithms:")
    sessions = repo.get_sessions_by_skill("Algorithms")
    print(f"Total Sessions: {len(sessions)}")

    # Apply decay
    engine.apply_decay_to_all(date.today())

    # Get focus
    focus = engine.get_daily_focus()

    print("\nCurrent Skills:")
    for skill in repo.list_skills():
        print(f"{skill.name}: {round(skill.strength, 2)}")

    print(f"\nToday's Focus: {focus.name}")


if __name__ == "__main__":
    main()
