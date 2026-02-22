from datetime import date

from core.models.skill import Skill
from core.engine.skill_engine import SkillEngine

from repository.in_memory_repository import InMemorySkillRepository

from core.scoring.skill_scoring import SkillScorer
from core.decay.decay_policy import DecayPolicy
from core.prioritization.priority_calculator import PriorityCalculator

from core.analytics.skill_analytics import SkillAnalytics
from services.strategic_simulator import StrategicSimulator


def main():
    repo = InMemorySkillRepository()

    # -----------------------------
    # Create Multiple Skills
    # -----------------------------
    repo.save_skill(Skill(name="Python", strength=50, role_weight=1.5))
    repo.save_skill(Skill(name="Algorithms", strength=30, role_weight=2.0))
    repo.save_skill(Skill(name="SystemDesign", strength=20, role_weight=1.8))

    # -----------------------------
    # Inject Dependencies
    # -----------------------------
    engine = SkillEngine(
        repository=repo,
        scorer=SkillScorer(),
        decay_policy=DecayPolicy(),
        priority_calculator=PriorityCalculator(),
    )

    # -----------------------------
    # Run Closed-Loop Strategic Simulation
    # -----------------------------
    simulator = StrategicSimulator(engine)

    simulator.run(
        start_date=date.today(),
        number_of_days=60,
    )

    # -----------------------------
    # Display Final Results
    # -----------------------------
    print("\nFinal Skill Strengths:")
    for skill in repo.list_skills():
        print(f"{skill.name}: {round(skill.strength, 2)}")

    focus = engine.get_daily_focus()
    print(f"\nCurrent Highest Priority Skill: {focus.name}")

    # -----------------------------
    # Analytics
    # -----------------------------
    analytics = SkillAnalytics(repo, SkillScorer())

    print("\nAnalytics Summary:")
    for skill in repo.list_skills():
        print(f"\n--- {skill.name} ---")
        print("Total Sessions:", analytics.total_sessions(skill.name))
        print("Consistency:", round(analytics.consistency_score(skill.name), 3))
        print("Average Delta:", round(analytics.average_delta(skill.name), 2))
        print("Momentum:", round(analytics.momentum_score(skill.name), 2))
        print("Volatility:", round(analytics.volatility(skill.name), 2))


if __name__ == "__main__":
    main()