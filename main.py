from datetime import date

from core.models.skill import Skill
from core.engine.skill_engine import SkillEngine

from repository.in_memory_repository import InMemorySkillRepository

from core.scoring.skill_scoring import SkillScorer
from core.decay.decay_policy import DecayPolicy
from core.prioritization.priority_calculator import PriorityCalculator

from core.analytics.skill_analytics import SkillAnalytics
from services.multi_day_simulator import MultiDaySimulator


def main():
    repo = InMemorySkillRepository()

    # Create skills
    python_skill = Skill(name="Python", strength=50, role_weight=1.5)
    algo_skill = Skill(name="Algorithms", strength=30, role_weight=2.0)

    repo.save_skill(python_skill)
    repo.save_skill(algo_skill)

    # Inject dependencies
    engine = SkillEngine(
        repository=repo,
        scorer=SkillScorer(),
        decay_policy=DecayPolicy(),
        priority_calculator=PriorityCalculator(),
    )

    # Run deterministic 30-day simulation
    simulator = MultiDaySimulator(engine)

    simulator.run(
        skill_name="Algorithms",
        start_date=date.today(),
        number_of_days=30,
    )

    # Analytics
    analytics = SkillAnalytics(repo, SkillScorer())

    print("\nSession History for Algorithms:")
    print("Total Sessions:", analytics.total_sessions("Algorithms"))

    print("\nCurrent Skills:")
    for skill in repo.list_skills():
        print(f"{skill.name}: {round(skill.strength, 2)}")

    focus = engine.get_daily_focus()
    print(f"\nToday's Focus: {focus.name}")

    print("\nAdvanced Metrics:")
    print("Consistency:", round(analytics.consistency_score("Algorithms"), 3))
    print("Recent Avg Delta:", round(analytics.recent_average_delta("Algorithms"), 2))
    print("Momentum:", round(analytics.momentum_score("Algorithms"), 2))
    print("Volatility:", round(analytics.volatility("Algorithms"), 2))


if __name__ == "__main__":
    main()
